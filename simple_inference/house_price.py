from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

import requests
import os
import numpy as np
import pandas as pd
from joblib import dump, load
import main
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

def train_model(data):
    main.get_data(data)
    if not os.path.isfile(data+'.csv'):
        raise HTTPException(status_code=500, detail="Unkown dataset: "+ data)
    df = pd.read_csv('house_price.csv')
    df.columns = df.columns.str.replace(' ', '_')
    X = df.drop('condition', axis=1)
    X = df.drop(['condition','date','street', 'city', 'statezip', 'country'], axis=1)
    y = df['condition']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    model = SVC()
    model.fit(X_train, y_train)
    expected_y  = y_test
    predicted_y = model.predict(X_test)
    model_metrics = metrics.classification_report(expected_y, predicted_y, output_dict=True,zero_division=1)
    dump(model, data+'_model.joblib')
    return model_metrics

class House_price(BaseModel):
    price : float = 313000.0
    bedrooms : float = 3.0
    bathrooms : float = 1.5
    sqft_living : int = 1340
    sqft_lot : int = 7912
    floors: float = 1.5
    waterfront : int = 0
    view : int= 0
    sqft_above : int = 1340
    sqft_basement : int = 0
    yr_built : int = 1955
    yr_renovated : int = 2005
    