import requests
import os
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy as db
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from joblib import dump, load


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Entrenar modelo"}


@app.get('/entrenar_modelo')
def train_model(model):
    if model == 'cover_type':
        cover_type_metrics = penguin_train.train_model('cover_type')
        return cover_type_metrics
    else:
        raise HTTPException(status_code=500, detail="Conjunto de datos desconocido: " + data)