#Operational Risk App – Task Delay Prediction
The Operational Risk App is a machine learning-based web application designed to predict the risk of task delays in project workflows. By combining predictive analytics with a robust rule-based logic layer, the tool identifies high-risk tasks early, allowing for proactive resource allocation and improved project planning.

Objectives
Predict Accuracy: Forecast operational task delay risks with high precision.

Early Identification: Spot high-risk tasks before they impact the critical path.

Proactive Decisions: Assist teams in data-driven decision-making.

Resource Optimization: Improve overall project planning and workload distribution.

Key Features
Hybrid Decision System: Integrates Scikit-learn models with rule-based logic for transparency.

Real-time Prediction: Instant risk classification via an interactive UI.

Confidence Scoring: Provides a probability-based score for every ML prediction.

Bulk Processing: Supports CSV uploads for batch analysis of project tasks.

Containerized: Fully Dockerized for easy deployment and portability.

Tech Stack
Language: Python

UI/Frontend: Streamlit

Machine Learning: Scikit-learn (Logistic Regression)

Data Processing: Pandas, NumPy

Model Persistence: Joblib

DevOps: Docker

Workflow & Logic
1. Data Preparation
The system processes operational data, including task priority, duration, complexity, and team workload. Categorical features are encoded for compatibility with the Machine Learning pipeline.

2. Hybrid Risk Engine
To ensure reliability, the app applies a High-Risk Override based on specific business logic:

Rule: If Past Delays Exist AND Team Workload is High, the task is flagged as High Risk regardless of the ML output.

If the rule is not triggered, the Logistic Regression model predicts the risk probability based on historical patterns.

3. Model Outputs
Risk Label: (High / Low)

Confidence Score: The probability percentage of the prediction.

Decision Source: Clarifies if the result was triggered by Rule-based logic or the ML model.

Docker Setup
1. Build the Image
Bash

docker build -t operational-risk-app .
2. Run the Container
Bash

docker run -p 8501:8501 operational-risk-app
3. Access the Application
Open your browser and go to: http://localhost:8501

Usage
Manual Entry: Use the sidebar or main form to input individual task parameters.

Batch Upload: Upload a .csv file containing task data to get a breakdown of risks across an entire department or project.
