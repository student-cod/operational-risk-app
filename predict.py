import pandas as pd
import joblib

# Load trained model
model = joblib.load("delay_risk_model.pkl")

# Manual encoding (must match training logic)
PRIORITY_MAP = {"Low": 0, "Medium": 1, "High": 2}
TEAM_LOAD_MAP = {"Low": 0, "Medium": 1, "High": 2}

def encode_inputs(df):
    df = df.copy()
    df["priority"] = df["priority"].map(PRIORITY_MAP)
    df["team_load"] = df["team_load"].map(TEAM_LOAD_MAP)
    return df

def rule_based_check(task):
    if task["past_delay"] == 1 and task["team_load"] == 2:
        return "High Risk", 0.95, "Rule-based decision"
    return None

def predict_risk(task_dict):
    # Rule-based first
    rule_result = rule_based_check(task_dict)
    if rule_result:
        return rule_result

    # ML-based
    df = pd.DataFrame([task_dict])
    df = encode_inputs(df)

    probs = model.predict_proba(df)[0]
    prediction = probs.argmax()
    confidence = probs[prediction]

    risk_label = "High Risk" if prediction == 1 else "Low Risk"
    return risk_label, confidence, "ML-based decision"
