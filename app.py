import streamlit as st
import pandas as pd
from predict import predict_risk

st.set_page_config(page_title="Operational Risk Predictor", layout="wide")

st.title("🚀 Operational Task Delay Risk Predictor")

# ---- Upload CSV ----
uploaded_file = st.file_uploader(
    "📂 Upload Operational Tasks CSV", type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # ---- Charts ----
    st.subheader("📊 Risk Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Risk Distribution")
        st.bar_chart(df["delay_risk"].value_counts())

    with col2:
        st.write("Estimated Days vs Risk")
        st.scatter_chart(
            df[["est_days", "delay_risk"]]
        )

    st.write("Team Load vs Risk")
    st.bar_chart(
        df.groupby("team_load")["delay_risk"].mean()
    )

    # ---- High Risk Count ----
    high_risk_count = df[df["delay_risk"] == 1].shape[0]
    st.metric("🚨 High Risk Tasks", high_risk_count)

# ---- Live Prediction ----
st.subheader("🧪 Predict New Task Risk")

priority = st.selectbox("Priority", ["Low", "Medium", "High"])
est_days = st.number_input("Estimated Days", 1, 30)
complexity = st.slider("Complexity", 1, 5)
team_load = st.selectbox("Team Load", ["Low", "Medium", "High"])
past_delay = st.selectbox("Past Delay", [0, 1])

if st.button("Predict Risk"):
    task = {
        "priority": priority,
        "est_days": est_days,
        "complexity": complexity,
        "team_load": team_load,
        "past_delay": past_delay,
    }

    risk, confidence, decision_type = predict_risk(task)

    st.subheader("🧠 Prediction Result")
    st.write(f"**{risk}**")
    st.write(f"Confidence: **{confidence * 100:.1f}%**")
    st.caption(decision_type)
