from pydantic import BaseModel
from typing import List, Dict, Any


class Task(BaseModel):
    goal: str
    steps: List[str]
    execution_plan: Dict[str, Any]
    outputs: Dict[str, Any] = {}

    @property
    def problem_type(self):
        return self.execution_plan.get("problem_type", "classification")
