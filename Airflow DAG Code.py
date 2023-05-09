from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'model_monitoring',
    default_args=default_args,
    description='End to End Model Monitoring',
    schedule_interval=timedelta(days=1),
)

# Define BashOperators to run the Python scripts for each task
task1 = BashOperator(
    task_id='connect_to_postgres',
    bash_command='python3 /path/to/script1.py',
    dag=dag,
)

task2 = BashOperator(
    task_id='data_preprocessing',
    bash_command='python3 /path/to/script2.py',
    dag=dag,
)

task3 = BashOperator(
    task_id='build_and_evaluate_model',
    bash_command='python3 /path/to/script3.py',
    dag=dag,
)

task4 = BashOperator(
    task_id='generate_reports',
    bash_command='python3 /path/to/script4.py',
    dag=dag,
)

task5 = BashOperator(
    task_id='monitor_drift',
    bash_command='python3 /path/to/script5.py',
    dag=dag,
)

task6 = BashOperator(
    task_id='docker_compose',
    bash_command='docker-compose up -d',
    dag=dag,
)

task7 = BashOperator(
    task_id='send_notification',
    bash_command='python3 /path/to/script6.py',
    dag=dag,
)

# Define the task dependencies
task1 >> task2 >> task3 >> task4 >> task5 >> task6 >> task7

