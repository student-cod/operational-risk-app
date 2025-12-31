# Operational Risk App – Task Delay Prediction

## Project Overview
The **Operational Risk App** is a machine learning–based web application designed to predict the risk of task delays in project workflows. It analyzes operational factors such as task priority, estimated duration, task complexity, team workload, and past delay history to classify tasks as **High Risk** or **Low Risk**.

The application uses a **hybrid approach**, combining rule-based logic with a machine learning model, and is built using **Streamlit** for an interactive user interface. The entire project is **Dockerized** and deployed on **Render** for public access.

---

## Objective
- **Predict Accuracy**: Accurately forecast operational task delay risks  
- **Early Detection**: Identify high-risk tasks early in the workflow  
- **Proactive Decisions**: Enable proactive planning and mitigation  
- **Resource Optimization**: Improve team workload and timeline management  

---

## Tools & Technologies Used

### Languages & Frameworks
- **Python** – Core programming language  
- **Streamlit** – Interactive web application framework  

### Machine Learning & Data Processing
- **Scikit-learn** – Logistic Regression model for risk classification  
- **Pandas & NumPy** – Data manipulation and numerical computation  
- **Joblib** – Model persistence and serialization  

### Deployment & DevOps
- **Docker** – Containerization for consistent environments  
- **Render** – Cloud platform for application deployment  

---

## Workflow Summary

### 1. Data Preparation
- Task-level operational data is prepared with relevant features  
- Categorical variables (Priority, Complexity, Workload) are encoded  
- Data is structured for real-time and batch predictions  

---

### 2. Rule-Based Logic
A **high-risk override** is applied when:

> **Past Delays Exist** AND **Team Workload is High**

This rule-based layer improves interpretability by catching known operational bottlenecks before relying solely on the ML model.

---

### 3. Machine Learning Prediction
- **Model Type**: Logistic Regression  
- **Prediction Output**: High Risk / Low Risk classification  
- **Confidence Score**: Probability-based confidence percentage  

---

### 4. Streamlit Application
- User-friendly UI for real-time predictions  
- CSV upload support for batch task analysis  
- Displays prediction results with confidence scores  

---

## Dockerization
The application is fully Dockerized to ensure portability and reproducibility.

**Docker Features:**
- Python-based Docker image  
- Dependency installation via `requirements.txt`  
- Streamlit exposed on port `8501`  

---

## Deployment
- Source code pushed to **GitHub**  
- Docker-based web service created on **Render**  
- Automatic build and deployment via Render  
- Public URL generated for live access  

---

## Live Deployment
| Platform | Link |
|--------|------|
| Render | https://operational-risk-app.onrender.com |

---

## How to Run Locally

### Using Docker
```bash
# Build Docker Image
docker build -t operational-risk-app .

# Run Docker Container
docker run -p 8501:8501 operational-risk-app


