# Airflow ML Pipeline – User Activity Trend Analysis

```yaml
project:
  name: Airflow ML Pipeline – User Activity Trend Analysis
  category: MLOps / Workflow Orchestration
  tool: Apache Airflow
  execution: Dockerized
  goal: >
    Build and orchestrate an end-to-end machine learning pipeline using
    Apache Airflow, covering data ingestion, preprocessing, model training,
    artifact generation, and inference.

overview:
  summary: >
    This repository demonstrates a production-style machine learning workflow
    orchestrated using Apache Airflow. The pipeline processes user behavior data,
    applies preprocessing, trains a clustering model, stores the model artifact,
    and performs inference through a structured DAG.
  key_features:
    - End-to-end Airflow DAG orchestration
    - Clear task dependencies and execution order
    - Model artifact creation and reuse
    - Containerized setup using Docker Compose
    - Reproducible local execution

airflow_pipeline:
  dag_name: Airflow_Lab1
  tasks:
    - name: load_data_task
      responsibility:
        - Load raw CSV dataset
        - Select relevant behavioral features
        - Serialize data using Base64 encoding

    - name: data_preprocessing_task
      responsibility:
        - Decode serialized data
        - Handle missing values
        - Apply MinMax scaling
        - Output processed dataset

    - name: build_save_model_task
      responsibility:
        - Train KMeans clustering models
        - Apply Elbow Method for cluster analysis
        - Save trained model artifact

    - name: load_model_task
      responsibility:
        - Load saved model
        - Preprocess test data
        - Generate cluster prediction

project_structure:
  root_directory: mlops-airflow-pipelines/
  layout:
    dags:
      airflow_lab1_dag.py: Airflow DAG definition
      src:
        __init__.py: Python package initializer
        lab.py: Machine learning logic
      data:
        online_shoppers_intention.csv: Training dataset
        test.csv: Inference dataset
      model:
        user_activity_trend_model.pkl: Trained model artifact
    plugins: Airflow plugins directory
    logs: Airflow execution logs
    docker-compose.yaml: Docker-based Airflow setup
    airflow.cfg: Airflow configuration
    webserver_config.py: Webserver settings
    .env: Environment variables
    .gitignore: Git ignore rules
    README.md: Project documentation

technology_stack:
  programming_language: Python 3.7
  orchestration: Apache Airflow 2.5.1
  machine_learning:
    - pandas
    - scikit-learn
    - kneed
  infrastructure:
    - Docker
    - Docker Compose
    - PostgreSQL
    - Redis

model_artifact:
  name: user_activity_trend_model.pkl
  generated_by: build_save_model_task
  stored_at: dags/model/
  purpose: >
    Persist trained clustering model for inference and reuse within the pipeline.

how_to_run_locally:
  prerequisites:
    - Docker installed
    - Docker Compose installed
    - Git installed

  steps:
    - step: clone_repository
      command: |
        git clone https://github.com/<your-username>/mlops-airflow-pipelines.git
        cd mlops-airflow-pipelines

    - step: start_airflow_services
      command: |
        docker-compose up -d

    - step: access_airflow_ui
      url: http://localhost:8080
      default_credentials:
        username: airflow
        password: airflow

    - step: trigger_pipeline
      instructions:
        - Unpause DAG Airflow_Lab1
        - Trigger DAG manually
        - Monitor Grid view and logs

execution_outcome:
  expected_results:
    - All DAG tasks complete successfully
    - Model artifact created
    - Inference executed successfully

use_case:
  relevance:
    - Demonstrates production-grade Airflow usage
    - Showcases ML pipeline orchestration
    - Suitable for Data Engineering and MLOps roles
