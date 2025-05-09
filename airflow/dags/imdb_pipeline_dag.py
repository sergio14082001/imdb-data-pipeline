from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Aseguramos que se pueda importar desde la carpeta scripts
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'scripts/')))

sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))


from scripts.download_data import main as download_data_main
from scripts.process_data import main as process_data_main
from scripts.joined_data import main as joined_data_main
from scripts.filter_top_movies import main as filter_top_movies_main

default_args = {
    'owner' : 'airflow',
    'start_date': datetime(2024,1,1), 
}

with DAG(
    dag_id = 'imdb_data_pipeline',
    default_args = default_args,
    schedule_interval = None,
    catchup = False,
    description = 'Pipeline IMDb con Pyspark y Airflow',
    tags = ['imdb','pipeline','pyspark']
) as dag:
    t1 = PythonOperator(
        task_id = 'download_data',
        python_callable = download_data_main
    )

    t2 = PythonOperator(
        task_id = 'process_data',
        python_callable = process_data_main
    )

    t3 = PythonOperator(
        task_id = 'join_data',
        python_callable = joined_data_main
    )

    t4 = PythonOperator(
        task_id = 'filter_top_movies',
        python_callable = filter_top_movies_main
    )

    t1 >> t2 >> t3 >> t4