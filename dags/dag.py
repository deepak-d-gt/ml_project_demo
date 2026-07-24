# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime

# from src.pipeline import run_pipeline

# with DAG(
#     dag_id="ml_pipeline_demo",
#     start_date=datetime(2026, 7, 25),
#     schedule=None,
#     catchup=False,
# ) as dag:

#     PythonOperator(
#         task_id="run_pipeline",
#         python_callable=run_pipeline,
#     )

# ingest = PythonOperator(
#     task_id="ingest",
#     python_callable=data_ingestion
# )

# preprocess = PythonOperator(
#     task_id="preprocess",
#     python_callable=preprocessing
# )

# train = PythonOperator(
#     task_id="train",
#     python_callable=model_building
# )

# evaluate = PythonOperator(
#     task_id="evaluate",
#     python_callable=model_evaluation
# )

# ingest >> preprocess >> train >> evaluate
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.data_ingestion import data_ingestion

with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2026, 7, 24),
    schedule="@daily", #None
    catchup=False,
) as dag:

    ingest = PythonOperator(
        task_id="ingest",
        python_callable=data_ingestion,
    )