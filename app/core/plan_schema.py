from pydantic import BaseModel
from typing import List, Dict, Optional

class PlanStep(BaseModel):
    step: str
    tool: str
    retry: int = 0
    notes: Optional[str] = None

class ExecutionPlan(BaseModel):
    ordered_steps: List[PlanStep]
