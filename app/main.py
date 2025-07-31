from fastapi import FastAPI
import os


from app.routers import message

app = FastAPI(
    title="LLM Backend API",
    description="API for generating responses using a Large Language Model (LLM)",
    version="1.0.0",
)

app.include_router(message.router)