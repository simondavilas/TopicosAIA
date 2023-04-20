from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

import sqlalchemy as db
from sqlalchemy import create_engine, text, insert
from sqlalchemy.ext.declarative import declarative_base
import pymysql

import requests
import os
import numpy as np
import pandas as pd
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC
from sklearn import metrics
from sqlalchemy import exc


def save_data(data):

    try:
        engine = create_engine(
            "mysql+pymysql://" + os.environ["USER_DB"] + ":" + os.environ["PASS_DB"] + "@" + os.environ[
                "IP_SERVER"] + "/" +
            os.environ["NAME_DB"])
        with engine.connect() as conn:
            data.to_sql(con=conn, index_label='id', name='feature', if_exists='append')
    except exc.SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error almacenando información para inferir del modelo.")


def inference_model(data):
    save_data(data)
