import pandas as pd
import numpy as np

np.random.seed(42)  # reproducibility

num_tasks = 500

data = {
    "task_id": [f"TASK_{i}" for i in range(1, num_tasks + 1)],
    "priority": np.random.choice(["Low", "Medium", "High"], num_tasks, p=[0.3, 0.4, 0.3]),
    "est_days": np.random.randint(1, 15, num_tasks),
    "complexity": np.random.randint(1, 6, num_tasks),
    "team_load": np.random.choice(["Low", "Medium", "High"], num_tasks, p=[0.3, 0.4, 0.3]),
    "past_delay": np.random.choice([0, 1], num_tasks, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# ---- Create delay risk using realistic rules ----
risk_score = (
    df["complexity"] * 0.4 +
    df["est_days"] * 0.3 +
    df["past_delay"] * 2
)

risk_score += df["team_load"].map({"Low": 0, "Medium": 1, "High": 2})
risk_score += df["priority"].map({"Low": 0, "Medium": 1, "High": 2})

df["delay_risk"] = (risk_score > np.percentile(risk_score, 65)).astype(int)

# Save dataset
df.to_csv("operational_tasks.csv", index=False)

print("✅ Dataset generated: operational_tasks.csv")
