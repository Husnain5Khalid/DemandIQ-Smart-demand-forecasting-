# 📈 Demand IQ – Retail Demand Forecasting Platform

> An end-to-end Machine Learning platform for retail demand forecasting using historical sales data, built with production-oriented ML pipelines and deployed through FastAPI.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![LightGBM](https://img.shields.io/badge/LightGBM-Model-success?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?style=for-the-badge&logo=amazonaws)

---

# 📖 Overview

Demand IQ is a production-oriented Machine Learning project designed to forecast retail product demand using historical sales, promotions, store metadata, and holiday information.

The project demonstrates the complete lifecycle of a machine learning application—from data preprocessing and feature engineering to model training, evaluation, prediction APIs, and deployment-ready architecture.

---

# 🚀 Features

- End-to-End ML Pipeline
- Exploratory Data Analysis (EDA)
- Advanced Feature Engineering
- Multiple Model Comparison
- Hyperparameter Tuning
- Modular Project Architecture
- Training Pipeline
- Prediction Pipeline
- Model Serialization
- FastAPI REST API
- Docker Containerization
- AWS Deployment Ready
- Logging & Exception Handling

---

# 🏗 Project Architecture

```
Demand-IQ

│
├── artifacts/
│
├── notebooks/
│
├── src/
│   ├── components/
│   │     ├── data_ingestion.py
│   │     ├── data_transformation.py
│   │     └── model_trainer.py
│   │
│   ├── pipelines/
│   │     ├── training_pipeline.py
│   │     └── prediction_pipeline.py
│   │
│   ├── utils/
│   │
│   ├── logger.py
│   ├── exception.py
│   └── config.py
│
├── app/
│     ├── main.py
│     ├── predictor.py
│     └── schemas.py
│
├── train.py
├── predict.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

Dataset includes:

- Historical Sales
- Store Information
- Holidays & Events
- Promotions
- Product Families

The objective is to predict daily sales for retail products.

---

# 🧹 Data Processing

The preprocessing pipeline includes:

- Missing Value Handling
- Date Feature Extraction
- Label Encoding
- One-Hot Encoding
- Numerical Scaling
- Feature Engineering
- Train/Validation Split

---

# 🤖 Machine Learning Models

The following regression models were evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- XGBoost
- CatBoost
- LightGBM ✅

---

# 🏆 Model Performance

| Model | MAE | RMSE | R² |
|-------|------|------|------|
| LightGBM | **70.62** | **243.45** | **0.967** |
| XGBoost | 75.96 | 263.56 | 0.961 |
| CatBoost | 82.42 | 266.81 | 0.960 |
| Ridge | 90.63 | 312.28 | 0.946 |
| Linear Regression | 91.80 | 316.01 | 0.944 |

**Best Model:** LightGBM

---

# ⚙️ Tech Stack

### Programming

- Python

### Machine Learning

- Scikit-learn
- LightGBM
- XGBoost
- CatBoost

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### API

- FastAPI

### Deployment

- Docker
- AWS

### Version Control

- Git
- GitHub

---

# 🚀 Running the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/Demand-IQ.git

cd Demand-IQ
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🏋️ Train Model

```bash
python train.py
```

---

# 🔮 Prediction

```bash
python predict.py
```

---

# 🌐 Run FastAPI

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker

Build Docker Image

```bash
docker build -t demand-iq .
```

Run Container

```bash
docker run -p 8000:8000 demand-iq
```

---

# ☁ AWS Deployment

Deployment-ready architecture prepared for AWS using Docker containers.

---

# 📈 Future Improvements

- MLflow Experiment Tracking
- CI/CD Pipeline
- Kubernetes Deployment
- Model Monitoring
- Automated Retraining
- Feature Store Integration

---

# 👨‍💻 Author

**Husnain Khalid**

Machine Learning Engineer

📧 husnainkhalidkhan6@gmail.com

🔗 LinkedIn: https://linkedin.com/in/husnain-khalid111


---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
