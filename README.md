# Operational Risk App – Task Delay Prediction

## Project Overview
The **Operational Risk App** is a machine learning–based web application designed to predict the risk of task delays in project workflows. It analyzes operational factors such as task priority, estimated duration, complexity, team workload, and past delay history to classify tasks as **High Risk** or **Low Risk**.

## Objective
* **Predict Accuracy**: Forecast operational task delay risks accurately.
* **Early Detection**: Identify high-risk tasks early in the workflow.
* **Proactive Decisions**: Assist teams in proactive decision-making.
* **Resource Optimization**: Improve project planning and resource allocation.

## Tools & Technologies Used

### Languages & Frameworks
* **Python**: Primary programming language.
* **Streamlit**: Web application framework for the interactive UI.

### Machine Learning & Data Processing
* **Scikit-learn**: Logistic Regression model for risk classification.
* **Pandas & NumPy**: Data manipulation and numerical processing.
* **Joblib**: Model persistence and serialization.

### Deployment & DevOps
* **Docker**: Containerization for environment consistency.
* **Cloud-ready**: Optimized for deployment on Render, Railway, or AWS.

---

## Workflow Summary

### 1. Data Preparation
* Task-level operational data is prepared with relevant features.
* Categorical features (e.g., Priority, Complexity) are encoded for ML compatibility.

### 2. Rule-Based Logic
High-risk override is applied when:
> **Past Delays Exist** AND **Team Workload is High**.

This hybrid approach improves transparency and decision confidence by catching known bottleneck patterns before they reach the model.

### 3. Machine Learning Prediction
* **Model Type**: Logistic Regression predicts the probability of a delay.
* **Confidence Score**: A percentage score calculated using prediction probabilities to show how certain the model is.

---

## How to Run

### Docker Setup
To build and run the application using Docker, use the following commands:

```bash
# Build Docker Image
docker build -t operational-risk-app .

# Run Docker Container
docker run -p 8501:8501 operational-risk-app
