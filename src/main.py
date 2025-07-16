import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="Schedule API Service",
    version="0.1.0",
    description="A FastAPI application to manage schedules with lessons and groups",
)


@app.get("/")
async def root():
    return {"message": "Schedule API Service"}
