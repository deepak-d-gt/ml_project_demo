from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from main import main

with DAG(
    dag_id="ml_pipeline_demo",
    start_date=datetime(2026, 7, 25),
    schedule=None,
    catchup=False,
) as dag:

    run_pipeline = PythonOperator(
        task_id="run_ml_pipeline",
        python_callable=main
    )