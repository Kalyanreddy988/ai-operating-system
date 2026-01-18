from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.metrics import accuracy_score, r2_score

def select_best_model(X_train, X_test, y_train, y_test, problem_type):
    results = {}

    if problem_type == "classification":
        models = {
            "LogisticRegression": LogisticRegression(max_iter=1000),
            "RandomForest": RandomForestClassifier(),
            "GradientBoosting": GradientBoostingClassifier()
        }
        metric_fn = accuracy_score

    else:  # regression
        models = {
            "LinearRegression": LinearRegression(),
            "RandomForest": RandomForestRegressor(),
            "GradientBoosting": GradientBoostingRegressor()
        }
        metric_fn = r2_score

    best_model = None
    best_score = -1

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        score = metric_fn(y_test, preds)

        results[name] = score

        if score > best_score:
            best_score = score
            best_model = (name, model)

    return {
        "best_model": best_model[0],
        "best_score": best_score,
        "all_results": results,
        "model_object": best_model[1]
    }
