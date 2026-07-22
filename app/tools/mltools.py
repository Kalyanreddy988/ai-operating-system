import os
import uuid
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import r2_score, accuracy_score

MODEL_DIR = "saved_models"
os.makedirs(MODEL_DIR, exist_ok=True)


def train_model(df, target_col, problem_type="auto"):
    # split features / target
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # encode categorical X
    X = pd.get_dummies(X, drop_first=True)

    # encode target if needed
    if y.dtype == "object":
        y = LabelEncoder().fit_transform(y)

    # ✅ SAFE auto-detection
    if problem_type == "auto":
        unique_count = len(np.unique(y))
        problem_type = "regression" if unique_count > 10 else "classification"

    # train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    if problem_type == "regression":
        models = {
            "LinearRegression": LinearRegression(),
            "RandomForestRegressor": RandomForestRegressor()
        }
        metric_name = "r2_score"
    else:
        models = {
            "LogisticRegression": LogisticRegression(max_iter=2000),
            "RandomForestClassifier": RandomForestClassifier()
        }
        metric_name = "accuracy"

    best_score = -1e9
    best_model = None
    best_model_name = None

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        score = (
            r2_score(y_test, preds)
            if problem_type == "regression"
            else accuracy_score(y_test, preds)
        )

        if score > best_score:
            best_score = score
            best_model = model
            best_model_name = name

    # save model
    model_id = str(uuid.uuid4())
    model_path = os.path.join(MODEL_DIR, f"{model_id}.joblib")
    joblib.dump(best_model, model_path)

    return {
    "model": best_model_name,
    "metric": metric_name,
    "score": round(float(best_score), 4),
    "confidence": "High" if best_score > 0.7 else "Medium",
    "model_id": model_id,   # ✅ REQUIRED
    "llm_explanation": {
        "summary": "Model trained successfully without runtime errors."
    }
}

