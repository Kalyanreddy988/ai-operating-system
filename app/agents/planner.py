from typing import Dict, List

def plan(goal: str = "Train ML Model") -> Dict:
    """
    Creates a high-level execution plan.
    The planner decides WHAT needs to be done,
    not HOW it will be executed.
    """

    execution_plan = {
        "goal": goal,
        "problem_type": "auto",
        "steps": [
            "load_data",
            "preprocess_data",
            "train_models",
            "evaluate_model",
            "save_model",
            "generate_report"
        ]
    }

    return execution_plan