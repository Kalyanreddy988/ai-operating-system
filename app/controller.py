from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.agents.executor import execute

router = APIRouter()

@router.post("/upload")
async def upload_dataset(
    file: UploadFile = File(...),
    goal: str = Form("Train ML Model")
):
    try:
        result = execute(file, goal)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))