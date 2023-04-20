import os
import requests
import pandas as pd
import glob
import csv
from sklearn.feature_selection import GenericUnivariateSelect, SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from configuration.env import DATASET_PATH, USER_DB, PASS_DB, IP_SERVER, NAME_DB


def load_data():
    # Ruta al conjunto de datos de entrenamiento
    _data_filepath = os.path.join(DATASET_PATH, 'covertype.train.csv')

    # Descarga del conjunto de datos
    os.makedirs(_data_root, exist_ok=True)
    if not os.path.isfile(_data_filepath):
        url = 'https://docs.google.com/uc?export= \
        download&confirm={{VALUE}}&id=1lVF1BCWLH4eXXV_YOJzjR7xZjj-wAGj9'
        r = requests.get(url, allow_redirects=True, stream=True)
        open(_data_filepath, 'wb').write(r.content)


def save_data_db(df, data):
    if data == 'cover_type':
        engine = create_engine(
            "mysql+pymysql://" + USER_DB + ":" + PASS_DB+ "@" + IP_SERVER + "/" + NAME_DB)
        with engine.connect() as conn:
            query = 'SELECT Elevation, Hillshade_9am, Hillshade_Noon, Horizontal_Distance_To_Fire_Points, Horizontal_Distance_To_Hydrology, Horizontal_Distance_To_Roadways, Slope, Soil_Type, Vertical_Distance_To_Hydrology, Wilderness_Area FROM ' + data
            df.to_sql(con=engine, index_label='id', name='cover_type', if_exists='append')
            pd.read_sql_query(sql=text(query), con=conn)
        return {"code": "ok", "description": "Datos almacenados en la tabla: " + data}
    else:
        raise HTTPException(status_code=500, detail="Conjunto de datos desconocido: " + data)


def process_info(data):
    load_data()
    # Leer todos los archivos csv en el sistema de archivos f
    csv_files = glob.glob(os.path.join(DATASET_PATH, "*train.csv"))
    dataframes = []
    for f in csv_files:
        lst = [*csv.DictReader(open(f))]
        if lst:
            df = pd.DataFrame(lst)
            df.cumsum()
            dataframes.append(df)

    training_dataset = pd.concat(dataframes, axis=0)

    # Eliminación de las características categóricas
    df_ct = training_dataset.drop(['Wilderness_Area', 'Soil_Type'], axis=1)

    # Selección de las mejores características
    y = df_ct['Cover_Type']
    X = df_ct.drop(['Cover_Type'], axis=1)

    select_k_best = SelectKBest(f_classif, k=8)
    X_new = select_k_best.fit_transform(X, y)

    # Creación de un nuevo dataframe con las 8 características seleccionadas
    features_names = select_k_best.get_feature_names_out()
    features_names.tolist()
    df_t = pd.DataFrame(X_new, columns=features_names)
    # Se reincorporan las columnas categorícas y la etiqueta al dataframe
    df_t.insert(len(df_t.columns), 'Wilderness_Area', training_dataset['Wilderness_Area'])
    df_t.insert(len(df_t.columns), 'Soil_Type', training_dataset['Soil_Type'])
    df_t.insert(len(df_t.columns), 'Cover_Type', y)
    save_data_db(df_t, data)
