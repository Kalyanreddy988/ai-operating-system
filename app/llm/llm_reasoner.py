def generate_llm_explanation(problem_type, score, cv_results, confidence):
    explanation = {}

    # ---------- SUMMARY ----------
    if problem_type == "regression":
        if score < 0:
            explanation["summary"] = (
                "The model was unable to learn strong predictive patterns from the dataset."
            )
        elif score < 0.5:
            explanation["summary"] = (
                "The model learned some patterns, but predictive power is limited."
            )
        else:
            explanation["summary"] = (
                "The model learned strong predictive relationships."
            )

    else:
        explanation["summary"] = (
            "The model was evaluated using classification accuracy."
        )

    # ---------- WHY SCORE ----------
    explanation["why_score_low"] = (
        "The target variable shows weak correlation with the available features, "
        "and the dataset may not contain enough informative signals."
    )

    # ---------- DATA QUALITY ----------
    explanation["data_quality"] = (
        "The dataset contains multiple categorical features and limited numeric depth, "
        "which can reduce model generalization."
    )

    # ---------- MODEL STABILITY ----------
    unstable = any(v["std"] > 0.05 for v in cv_results.values())

    explanation["model_stability"] = (
        "Model performance varies across folds, indicating instability."
        if unstable else
        "Model performance is relatively stable across folds."
    )

    # ---------- RECOMMENDATIONS ----------
    explanation["recommendations"] = [
        "Increase dataset size",
        "Add more domain-relevant numerical features",
        "Perform advanced feature engineering",
        "Experiment with ensemble models"
    ]

    explanation["confidence"] = confidence

    return explanation
