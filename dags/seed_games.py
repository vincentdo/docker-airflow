from application.scrape.sportradar import sportradar_wrapper

from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2017, 7, 1)
}

dag = DAG('scheduled_tasks', default_args=default_args)

seed_games_task = PythonOperator(
    task_id='seed_games_task',
    provide_context=False,
    python_callable=sportradar_wrapper,
    dag=dag)
