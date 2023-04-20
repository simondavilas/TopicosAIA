from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

import requests
import os
import numpy as np
import pandas as pd
from joblib import dump, load
import cover_type_inference
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import sqlalchemy as db
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
import pymysql

app = FastAPI()

@app.post("/predict_model")
async def do_inference(cover_type_inference : cover_type_inference.CoverType, model:str='cover_type'):
    if not os.path.isfile('/predict/model/' + model +'_model.joblib'):
        raise HTTPException(status_code=500, detail="Modelo desconocido: "+ model+" Intente entrenar primero el modelo.")
    model_loaded = load('/predict/model/' + model +'_model.joblib')
    df = pd.DataFrame([cover_type_inference.dict()])
    prediction = int(model_loaded.predict(df)[0])
    df['Cover_Type'] = prediction
    engine = create_engine(
            "mysql+pymysql://" + os.environ["USER_DB"] + ":" + os.environ["PASS_DB"] + "@" + os.environ["IP_SERVER"] + "/" + os.environ["NAME_DB"])
        with engine.connect() as conn:
            df.to_sql(con=engine, index_label='id', name='cover_type', if_exists='append')
    return prediction