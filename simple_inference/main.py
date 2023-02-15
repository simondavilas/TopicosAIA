from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

import requests
import os
import numpy as np
import pandas as pd
from joblib import dump, load
import wine
import house_price
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics


url_wine='https://docs.google.com/uc?export=download&id=1ZsJWYHxcEdJQdb62diQf8o3fvXFawt1a'
url_house_price='https://docs.google.com/uc?export=download&id=1WsTJN-u4YRrPKqJTp8h8iUSAdfJC8_qn'

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def get_data(data):
    if data=='wine' or data=='house_price':
        if not os.path.isfile(data+'.csv'):
            url = url_wine if data == 'wine' else url_house_price
            r = requests.get(url, allow_redirects=True)
            open(data+'.csv', 'wb').write(r.content)
    else:
        raise HTTPException(status_code=500, detail="Unkown dataset: "+ data)

@app.get('/select_model')
def select_model(model):
    if model == 'wine':
        wine_metrics = wine.train_model('wine')
        return wine_metrics 
    elif model == 'house_price':
        house_metrics = house_price.train_model('house_price')
        return house_metrics
    else:
        raise HTTPException(status_code=500, detail="Unkown dataset: "+ data)
        


@app.post("/do_inference/wine")
async def do_inference(wine : wine.Wine, model:str='wine'):
    if not os.path.isfile(model+'_model.joblib'):
        raise HTTPException(status_code=500, detail="Unkown model: "+ model+" Try to train model first.")
    model_loaded = load(model+'_model.joblib')
    return int(model_loaded.predict(pd.DataFrame([wine.dict()]))[0])

@app.post("/do_inference/house_price")
async def do_inference(house_price : house_price.House_price, model:str='house_price'):
    if not os.path.isfile(model+'_model.joblib'):
        raise HTTPException(status_code=500, detail="Unkown model: "+ model+" Try to train model first.")
    model_loaded = load(model+'_model.joblib')
    return int(model_loaded.predict(pd.DataFrame([house_price.dict()]))[0])


