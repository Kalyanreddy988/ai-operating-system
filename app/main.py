from fastapi import FastAPI
from app.controller import router

app = FastAPI(
    title="AI Operating System",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Operating System Running Successfully"}

@app.get("/health")
def health():
    return {"status": "healthy"}