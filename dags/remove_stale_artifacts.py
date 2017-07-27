from application.scheduled.prune import remove_stale_artifacts

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

remove_stale_artifacts_task = PythonOperator(
    task_id='remove_stale_artifacts',
    provide_context=False,
    python_callable=remove_stale_artifacts,
    dag=dag)
