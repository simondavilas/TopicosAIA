from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from configuration.env import DATASET_PATH
import sqlalchemy as db
from sqlalchemy import create_engine, text, update
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from pathlib import Path
import requests
import os
import numpy as np
import pandas as pd
from joblib import dump, load
from sqlalchemy import exc


def get_data(data):
    engine = create_engine(
        "mysql+pymysql://" + USER_DB + ":" + PASS_DB + "@" + IP_SERVER + "/" + NAME_DB)
    with engine.connect() as conn:
        query = 'SELECT Elevation, Hillshade_9am, Hillshade_Noon, Horizontal_Distance_To_Fire_Points, Horizontal_Distance_To_Hydrology, Horizontal_Distance_To_Roadways, Slope, Soil_Type, Vertical_Distance_To_Hydrology, Wilderness_Area FROM ' + data \
                + ' WHERE processed=0'
        if db.inspect(conn).has_table('data'):
            df_db = pd.read_sql_query(sql=text(query), con=conn)
            return df_db
        else:
            raise HTTPException(status_code=500, detail="No se encontró en la base de datos la tabla: " + data)


def update_data():
    try:
        engine = create_engine(
            "mysql+pymysql://" + os.environ["USER_DB"] + ":" + os.environ["PASS_DB"] + "@" + os.environ[
                "IP_SERVER"] + "/" +
            os.environ["NAME_DB"])
        with engine.connect() as conn:
            stmt = (
                update(feature).where(feature.c.processed == 0).values(processed=1)
            )
            conn.execute(stmt)
    except exc.SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error almacenando información para inferir del modelo.")


def save(data):
    feature_data = get_data(data)
    filepath = Path(DATASET_PATH + now() + '.train.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    feature_data.to_csv(filepath)
    update_data()
