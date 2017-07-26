from application.scheduled.prune import expire_outcomes, remove_stale_artifacts
from application.scrape.sportradar import sportradar_wrapper, sportradar_check_existing_games

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
    'start_date': datetime(2015, 6, 1)
}

dag = DAG('scheduled_tasks', default_args=default_args)

# remove_stale_artifacts_task = PythonOperator(
#     task_id='remove_stale_artifacts',
#     provide_context=False,
#     python_callable=remove_stale_artifacts,
#     dag=dag)
#
# expire_outcomes_task = PythonOperator(
#     task_id='expire_outcomes_task',
#     provide_context=False,
#     python_callable=expire_outcomes,
#     dag=dag)

# complete_events_task = PythonOperator(
#     task_id='complete_events_task',
#     provide_context=True,
#     python_callable=sportradar_check_existing_games,
#     dag=dag)

seed_games_task = PythonOperator(
    task_id='seed_games_task',
    provide_context=False,
    python_callable=sportradar_wrapper,
    dag=dag)
