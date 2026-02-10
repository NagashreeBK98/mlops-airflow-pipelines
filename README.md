# User Activity Trend Analysis Pipeline
**End-to-End ML Workflow Orchestration with Apache Airflow**

---

## Overview
This project implements a production-grade machine learning pipeline for user activity trend analysis using Apache Airflow. The pipeline orchestrates the complete workflow from data ingestion to model deployment, demonstrating real-world MLOps practices including automated workflow management, task dependency handling, and artifact persistence.

Built with a containerized Airflow environment, this system showcases scalable data processing and machine learning orchestration patterns used in modern data engineering and MLOps systems.

---

## Project Structure

```
mlops-airflow-pipelines/
├── dags/
│   ├── airflow_lab1_dag.py
│   ├── src/
│   │   ├── __init__.py
│   │   └── lab.py
│   ├── data/
│   │   ├── online_shoppers_intention.csv
│   │   └── test.csv
│   └── model/
│       └── user_activity_trend_model.pkl
├── config/
│   └── airflow.cfg
├── plugins/
├── logs/
├── docker-compose.yaml
├── webserver_config.py
├── .env
├── .gitignore
└── README.md
```

---

## Pipeline Architecture

### DAG: `Airflow_Lab1`

The pipeline consists of four sequential tasks that form a complete ML workflow:

**1. Data Ingestion (`load_data_task`)**
   - Loads raw CSV dataset containing user activity metrics
   - Performs feature selection based on behavioral patterns
   - Serializes data for efficient inter-task communication using XCom

**2. Data Processing (`data_preprocessing_task`)**
   - Handles missing values and data quality issues
   - Applies MinMax normalization for feature scaling
   - Prepares dataset for clustering analysis

**3. Model Training (`build_save_model_task`)**
   - Trains KMeans clustering models with multiple configurations
   - Implements Elbow Method for optimal cluster determination
   - Persists trained model artifact for reusability

**4. Model Inference (`load_model_task`)**
   - Loads persisted model from artifact storage
   - Processes test data through preprocessing pipeline
   - Generates cluster predictions for new user activity data

---

## Machine Learning Implementation

The ML logic (`lab.py`) implements:
- **Feature Engineering**: Behavioral metric selection and transformation
- **Data Preprocessing**: Scaling, normalization, and missing value handling
- **Clustering Algorithm**: KMeans with automated cluster optimization
- **Model Persistence**: Pickle-based artifact storage for model reuse
- **Inference Pipeline**: End-to-end prediction workflow

### Key Technical Features
- Automated hyperparameter tuning using Elbow Method
- Scalable preprocessing pipeline
- Model versioning and artifact management
- Reproducible ML workflows

---

## Technology Stack

| Component | Technology |
|-----------|-----------|
| **Orchestration** | Apache Airflow 2.5.1 |
| **Language** | Python 3.7 |
| **ML Framework** | scikit-learn, pandas, kneed |
| **Infrastructure** | Docker, Docker Compose |
| **Database** | PostgreSQL |
| **Message Broker** | Redis |
| **Containerization** | Docker Engine |

---

## Getting Started

### Prerequisites
- Docker Desktop or Docker Engine
- Docker Compose
- Git

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/NagashreeBK98/mlops-airflow-pipelines.git
   cd mlops-airflow-pipelines
   ```

2. **Start Airflow services**
   ```bash
   docker-compose up -d
   ```

3. **Verify deployment**
   ```bash
   docker ps
   ```
   You should see containers for webserver, scheduler, postgres, and redis running.

4. **Access Airflow UI**
   - URL: `http://localhost:8080`
   - Username: `airflow`
   - Password: `airflow`

### Running the Pipeline

1. Navigate to the Airflow web interface
2. Locate the `Airflow_Lab1` DAG in the dashboard
3. Toggle the DAG to **ON** (unpause)
4. Click the **Trigger DAG** button (▶️ icon)
5. Monitor execution in real-time:
   - **Grid View**: Task execution timeline and status
   - **Graph View**: Visual task dependencies
   - **Logs**: Detailed execution logs for each task

### Expected Results

✅ All tasks complete successfully in sequence  
✅ Model artifact saved to `dags/model/user_activity_trend_model.pkl`  
✅ Cluster predictions generated for test dataset  
✅ Execution logs available for debugging and monitoring  

---

## Key Features

- **Automated Workflow Orchestration**: End-to-end pipeline automation with dependency management
- **Scalable Architecture**: Containerized deployment for easy scaling and reproducibility
- **Model Artifact Management**: Persistent storage and versioning of trained models
- **Monitoring & Observability**: Comprehensive logging and task execution tracking
- **Production-Ready**: Demonstrates MLOps best practices for real-world deployment

---

## Pipeline Visualization

The DAG provides multiple views for monitoring:
- **Graph View**: Visualize task dependencies and data flow
- **Grid View**: Track execution history across multiple runs
- **Gantt Chart**: Analyze task duration and identify bottlenecks
- **Code View**: Inspect DAG definition and task logic

---

## Use Cases

This pipeline architecture is applicable to:
- Customer segmentation and behavioral analysis
- User activity pattern recognition
- E-commerce trend analysis
- Automated ML model retraining workflows
- Data quality monitoring pipelines

---

## Future Enhancements

- [ ] Integration with cloud storage (S3/GCS) for data persistence
- [ ] Model performance monitoring and drift detection
- [ ] A/B testing framework for model comparison
- [ ] Real-time inference API deployment
- [ ] Advanced alerting and notification system
- [ ] Integration with MLflow for experiment tracking

---

## Contact

**Nagashree BK**  
[GitHub](https://github.com/NagashreeBK98) | [LinkedIn](https://www.linkedin.com/in/nagashreebk)

---

## License

This project is open source and available under the MIT License.
