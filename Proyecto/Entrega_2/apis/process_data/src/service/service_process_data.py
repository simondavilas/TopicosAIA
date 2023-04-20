from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

import requests
import os
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy as db
import core.process_data as process
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base

from joblib import dump, load

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Procesamiento"}


@app.get('/procesar-info')
def process_info(data):
    if model == 'cover_type':
        process.process_info('cover_type')
    else:
        raise HTTPException(status_code=500, detail="Conjunto de datos desconocido: " + data)