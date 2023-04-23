import os

import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException
from joblib import load
import commons.logs.logger as log
import core.inference_core as inference_process
import data.cover_type_inference as cover_type_inference
from configuration.env import MODEL_PATH

app = FastAPI()

logger = log.get_logger('inference-component')


@app.post("/predict_model")
async def do_inference(inference: cover_type_inference.CoverType, model: str = 'cover_type'):
    logger.info('Iniciando inferencia con modelo %s', model)
    if not os.path.isfile(MODEL_PATH + model + '_model.joblib'):
        raise HTTPException(status_code=500,
                            detail="Modelo desconocido: " + model + " Intente entrenar primero el modelo.")
    model_loaded = load(MODEL_PATH + model + '_model.joblib')
    inference_data = inference.dict()
    inference_data["processed"] = 0
    inference_data["Cover_Type"] = int(model_loaded.predict(pd.DataFrame([inference.dict()]))[0])
    inference_process.inference_model(pd.DataFrame([inference_data]))
    return inference_data["Cover_Type"]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)