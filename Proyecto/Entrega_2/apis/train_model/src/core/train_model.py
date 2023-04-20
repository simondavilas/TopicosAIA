import sqlalchemy as db
import requests
import os
import numpy as np
import pandas as pd
import pymysql
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from configuration.env import NAME_DB, PASS_DB, IP_SERVER, USER_DB, MODEL_PATH


def get_data(data):
    if data == 'cover_type':

        engine = create_engine(
            "mysql+pymysql://" + USER_DB + ":" + PASS_DB + "@" + IP_SERVER + "/" + NAME_DB)
        with engine.connect() as conn:
            query = 'SELECT Elevation, Hillshade_9am, Hillshade_Noon, Horizontal_Distance_To_Fire_Points, Horizontal_Distance_To_Hydrology, Horizontal_Distance_To_Roadways, Slope, Soil_Type, Vertical_Distance_To_Hydrology, Wilderness_Area FROM ' + data
            if db.inspect(conn).has_table('cover_type'):
                df_db = pd.read_sql_query(sql=text(query), con=conn)
                return df_db
            else:
                raise HTTPException(status_code=500, detail="No se encontró en la base de datos la tabla: " + data)
    else:
        raise HTTPException(status_code=500, detail="Conjunto de datos desconocido: " + data)


def versioning_model(full_path):
    version_full_path = None
    if os.path.isfile(full_path):
        csv_files = glob.glob(os.path.join(MODEL_PATH, "*model.joblib"))
        versions = []
        for f in csv_files:
            arr_idx_f = f.split("_")
            version = arr_idx_f[1]
            if version != "latest":
                versions.append(int(version))

        max_version = 0
        if len(versions) != 0:
            max_version = np.max(versions) + 1

        version_full_path = MODEL_PATH + 'cover_type' + '_' + max_version + '_model.joblib'
        os.renames(full_path, version_full_path)

    return full_path, version_full_path


def save_model(df):
    engine = create_engine(
        "mysql+pymysql://" + os.environ["USER_DB"] + ":" + os.environ["PASS_DB"] + "@" + os.environ["IP_SERVER"] + "/" +
        os.environ["NAME_DB"])
    with engine.connect() as conn:
        df.to_sql(con=conn, index_label='id', name='model', if_exists='append')


def train_model(data):
    df = get_data(data)
    df = df.dropna()
    df['Wilderness_Area'].replace(['Cache', 'Commanche', 'Neota', 'Rawah'],
                                  [0, 1, 2, 3], inplace=True)
    df['Soil_Type'].replace(
        ['C2702', 'C2703', 'C2704', 'C2705', 'C2706', 'C2717', 'C3501', 'C3502', 'C4201', 'C4703', 'C4704', 'C4744',
         'C4758', 'C5101', 'C6101', 'C6102', 'C6731', 'C7101', 'C7102', 'C7103', 'C7201', 'C7202', 'C7700', 'C7701',
         'C7702', 'C7709', 'C7710', 'C7745', 'C7746', 'C7755', 'C7756', 'C7757', 'C7790', 'C8703', 'C8707', 'C8708',
         'C8771', 'C8772', 'C8776', 'C5151'],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39], inplace=True)
    X = df.drop('Cover_Type', axis=1)
    y = df['Cover_Type']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
    model = SVC()
    model.fit(X_train, y_train)
    expected_y = y_test
    predicted_y = model.predict(X_test)
    model_metrics = metrics.classification_report(expected_y, predicted_y, output_dict=True, zero_division=1)
    model_full_path, version_full_path = versioning_model(MODEL_PATH + data + '_latest_model.joblib')
    dump(model, model_full_path)
    data = [[model_full_path[19:], now()], [version_full_path[19:], now()]]
    d_final = pd.DataFrame(data, columns=['model', 'update_date'])
    save_model(d_final)
    return model_metrics
