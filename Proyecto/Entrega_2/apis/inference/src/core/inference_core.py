import commons.logs.logger as log
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy import exc

from configuration.env import NAME_DB, PASS_DB, USER_DB, IP_SERVER

logger = log.get_logger('inference-save-component')


def save_data(data):
    logger.info('Iniciando persistencia de caracteristicas para inferir cover_type')
    try:
        engine = create_engine("mysql+pymysql://" + USER_DB + ":" + PASS_DB + "@" + IP_SERVER + "/" + NAME_DB)
        with engine.connect() as conn:
            data.to_sql(con=conn, index_label='id', name='feature', if_exists='append')
    except exc.SQLAlchemyError as error:
        logger.error(error)
        raise HTTPException(status_code=500, detail="Error almacenando información para inferir del modelo.")


def inference_model(data):
    save_data(data)
    logger.info('finalizó exitosamente persistencia de caracteristicas en inferencia')
