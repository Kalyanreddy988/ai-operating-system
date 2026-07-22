from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.agents.planner import plan
from app.agents.decomposer import decompose
from app.agents.executor import execute

router = APIRouter()


@router.post("/upload")
async def upload_csv(
    file: UploadFile = File(...),
    goal: str = Form(default="Train ML Model")
):
    try:

        execution_plan = plan(goal)

        tasks = decompose(execution_plan)

        result = execute(file, tasks)

        return {
            "goal": goal,
            "plan": execution_plan,
            "execution": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))