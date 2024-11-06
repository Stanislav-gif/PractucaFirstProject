from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PC(BaseModel):
    id: int
    screen: Optional[str] = None
    keyboard: Optional[str] = None
    mouse: Optional[str] = None
    processor: Optional[str] = None
    video_card: Optional[str] = None

repo: List[PC] = []

@app.get("/pc", response_model=List[PC])
def get_ps():
    return repo
