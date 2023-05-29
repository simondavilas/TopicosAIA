import os
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from airflow import DAG
from airflow.operators.bash import BashOperator 
from airflow.operators.python import PythonOperator
from datetime import datetime
from sklearn.model_selection import train_test_split

_data_filepath = ""

def download_data():
    ## download the dataset
    # Directory of the raw data files
    _data_root = './data/Diabetes'
    # Path to the raw training data
    _data_filepath = os.path.join(_data_root, 'Diabetes.csv')
    # Download data
    os.makedirs(_data_root, exist_ok=True)
    if not os.path.isfile(_data_filepath):
        #https://archive.ics.uci.edu/ml/machine-learning-databases/covtype/
        url = 'https://docs.google.com/uc?export= \
            download&confirm={{VALUE}}&id=1k5-1caezQ3zWJbKaiMULTGq-3sz6uThC'
        r = requests.get(url, allow_redirects=True, stream=True)
        open(_data_filepath, 'wb').write(r.content)



def feed_raw_data():
    diabetes_dataset =  pd.read_csv(_data_filepath)
    diabetes_train, diabetes_test = train_test_split(diabetes_dataset, test_size = 0.3, random_state = 99, stratify=diabetes_dataset['readmitted'])
    diabetes_test, diabetes_validation = train_test_split(diabetes_test, test_size = 0.25, random_state = 99, stratify=diabetes_dataset['readmitted'])

    try:
        engine = create_engine('postgresql+psycopg2://topicosIA:topicosIA@data-db-mlfow-svc/data-mlfow')
        with engine.connect() as conn:
            n = 15000
            diabetes_test.to_sql(con=engine, index_label='id', name='diabetes_test', if_exists='replace')
            diabetes_validation.to_sql(con=engine, index_label='id', name='diabetes_validation', if_exists='replace')
            list_df_train = [diabetes_train[i:i+n] for i in range(0,len(diabetes_train),n)]

            for df in list_df_train:
                df.to_sql(con=engine, index_label='id', name='diabetes_train', if_exists='append')
        
    except Exception as error:
        print(error)
    


with DAG (dag_id= "feed_data",
          description="Utilizando bash operator",
          start_date=datetime (2023,5,1)) as dag:
        
    t1 = PythonOperator (task_id="downloadDataTask",
                         python_callable=download_data)
    t2 = PythonOperator (task_id="loadDB",
                         python_callable=feed_raw_data)
    
    t1 >> t2
