import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load data
df = pd.read_csv("operational_tasks.csv")

# Encode categorical columns
encoder = LabelEncoder()
df["priority"] = encoder.fit_transform(df["priority"])
df["team_load"] = encoder.fit_transform(df["team_load"])

# Features & target
X = df.drop(columns=["task_id", "delay_risk"])
y = df["delay_risk"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))



joblib.dump(model, "delay_risk_model.pkl")
print("Model saved successfully!")

