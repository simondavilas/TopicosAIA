import requests
import os
import numpy as np
import pandas as pd
import core.save_data_core as sd
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

app = FastAPI()


@app.get("/save_data")
async def save_data():
    sd.save("feature")
    return {"code": "ok", "description": "Se agrego exitosamente archivos al conjunto de datos"}
