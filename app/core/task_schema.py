from pydantic import BaseModel
from typing import List, Optional, Dict

class Task(BaseModel):
    task_id: str
    user_goal: str
    task_type: str
    input_files: Optional[List[str]] = []
    steps: Optional[List[str]] = []
    current_step: Optional[int] = 0
    outputs: Optional[Dict] = {}
    confidence: Optional[float] = None
    status: str = "PENDING"
