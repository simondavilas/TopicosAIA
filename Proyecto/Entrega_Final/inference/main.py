from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

import os
import requests
import pandas as pd
import diabetes
import mlflow

os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://minio-puj.dev.ri.appgate.com/"
os.environ['AWS_ACCESS_KEY_ID'] = 'admin'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'supersecret'



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/do_inference/")
async def do_inference(diabetes : diabetes.Diabetes, model:str='diabetes'):
    # if not os.path.isfile(model+'_model.joblib'):
    mlflow.set_tracking_uri("http://mlflow-puj.dev.ri.appgate.com/")
    model_logged = 'runs:/a3a1f63e37c74c8eb2dbd924f3246a9d/model'
    model = mlflow.pyfunc.load_model(model_logged)
    # raise HTTPException(status_code=500, detail="Unkown model: "+ model+" Try to train model first.")    
    
    
    return int(model.predict(pd.DataFrame([diabetes.dict(by_alias=True)]))[0])