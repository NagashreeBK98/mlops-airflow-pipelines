from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.lab import load_data, data_preprocessing, build_save_model, load_model_elbow

default_args = {
    "owner": "Nagashree",
    "start_date": datetime(2026, 1, 15),
    "retries": 0,
}

with DAG(
    dag_id="Airflow_Lab1",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    load_data_task = PythonOperator(
        task_id="load_data_task",
        python_callable=load_data,
    )

    data_preprocessing_task = PythonOperator(
        task_id="data_preprocessing_task",
        python_callable=lambda ti: data_preprocessing(
            ti.xcom_pull(task_ids="load_data_task")
        ),
    )

    build_save_model_task = PythonOperator(
        task_id="build_save_model_task",
        python_callable=lambda ti: build_save_model(
            ti.xcom_pull(task_ids="data_preprocessing_task"),
            "user_activity_trend_model.pkl",
        ),
    )

    load_model_task = PythonOperator(
        task_id="load_model_task",
        python_callable=lambda ti: load_model_elbow(
            "user_activity_trend_model.pkl",
            ti.xcom_pull(task_ids="build_save_model_task"),
        ),
    )

    load_data_task >> data_preprocessing_task >> build_save_model_task >> load_model_task