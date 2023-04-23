import calendar
import time
import commons.logs.logger as log
from pathlib import Path
import pandas as pd
import sqlalchemy as db
from fastapi import HTTPException
from sqlalchemy import create_engine, text, update, MetaData
from configuration.env import USER_DB, PASS_DB, IP_SERVER, NAME_DB

from configuration.env import DATASET_PATH

logger = log.get_logger('save data component')


def get_data(data):
    logger.info('consultando información de caracteristicas no procesadas')
    try:
        engine = create_engine(
            "mysql+pymysql://" + USER_DB + ":" + PASS_DB + "@" + IP_SERVER + "/" + NAME_DB)
        with engine.connect() as conn:
            query = 'SELECT Elevation, Hillshade_9am, Hillshade_Noon, Horizontal_Distance_To_Fire_Points, ' \
                    'Horizontal_Distance_To_Hydrology, Horizontal_Distance_To_Roadways, Slope, Soil_Type, ' \
                    'Vertical_Distance_To_Hydrology, Wilderness_Area, Cover_Type FROM ' + data \
                    + ' WHERE processed=0'
            if db.inspect(conn).has_table(data):
                df_db = pd.read_sql_query(sql=text(query), con=conn)
                return df_db
            else:
                raise HTTPException(status_code=500, detail="No se encontró en la base de datos la tabla: " + data)
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=500, detail="Error almacenando información para inferir del modelo.")


def update_data():
    try:
        engine = create_engine(
            "mysql+pymysql://" + USER_DB + ":" + PASS_DB + "@" + IP_SERVER + "/" + NAME_DB)
        meta = MetaData()
        MetaData.reflect(meta, bind=engine)
        with engine.connect() as conn:
            feature = meta.tables['feature']
            stmt = (
                update(feature).where(feature.c.processed == 0).values(processed=1)
            )
            conn.execute(stmt)
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=500, detail="Error almacenando información para inferir del modelo.")


def save(data):
    feature_data = get_data(data)
    current_time = time.gmtime()
    time_stamp = calendar.timegm(current_time)
    filepath = Path(DATASET_PATH + str(time_stamp) + '.train.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    feature_data.to_csv(filepath)
    update_data()
