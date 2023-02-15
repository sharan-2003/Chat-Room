
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def root():
    return "hello world"
