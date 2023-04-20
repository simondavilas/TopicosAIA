import data.cover_type_inference as cover_type_inference
import requests
import os
import numpy as np
import pandas as pd
import core.inference_core as inference_process
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from configuration.env import MODEL_PATH

app = FastAPI()


@app.post("/predict_model")
async def do_inference(inference: cover_type_inference.CoverType, model: str = 'cover_type'):
    if not os.path.isfile(MODEL_PATH + model + '_model.joblib'):
        raise HTTPException(status_code=500,
                            detail="Modelo desconocido: " + model + " Intente entrenar primero el modelo.")
    model_loaded = load(MODEL_PATH + model + '_model.joblib')
    inference_data = inference.dict()
    inference_data["processed"] = 0
    inference_process.inference_model(pd.DataFrame.from_dict(inference_data))
    return int(model_loaded.predict(pd.DataFrame([inference.dict()]))[0])
