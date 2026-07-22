def plan(steps):
    return {
        "problem_type": "classification",
        "model_candidates": [
            "LogisticRegression",
            "RandomForest"
        ],
        "metrics": ["accuracy"]
    }
