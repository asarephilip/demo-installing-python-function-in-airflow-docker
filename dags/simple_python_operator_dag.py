from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from functions.refresh_view import hello  # function from GitHub repository

default_args = {
    'owner': 'phil',
    'retries': 5,
    'retry_delay': timedelta(2),
}


def greet(name='name', age=1):
    return f"Hello world. My name is {name} and I am {age} years old."


with DAG(
        dag_id='simple_python_operator',
        default_args=default_args,
        description='A simple python operator',
        start_date=datetime(2023, 11, 23, 0),
        schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='run_remote_function_in_airflow_dag',
        op_kwargs={'who': 'phil'},
        python_callable=hello,
    )

task1
