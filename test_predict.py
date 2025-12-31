from predict import predict_risk

test_task = {
    "priority": 1,
    "est_days": 6,
    "complexity": 3,
    "team_load": 2,  # High
    "past_delay": 1
}

print(predict_risk(test_task))
