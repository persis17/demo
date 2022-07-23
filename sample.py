from types import DynamicClassAttribute
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.version import version
from airflow.hooks.base_hook import BaseHook
from datetime import datetime, timedelta

def testing_dag():
    print("Am a test_dag")

with DAG('sample_dag',
    start_date=datetime(2022, 1, 1),
    max_active_runs=3,
    schedule_interval='@once',  # https://airflow.apache.org/docs/stable/scheduler.html#dag-runs
    catchup=False # enable if you don't want historical dag runs to run
    ) as dag:

    task1= PythonOperator(
        task_id = 'task_1',
        python_callable = testing_dag
    )

    task1