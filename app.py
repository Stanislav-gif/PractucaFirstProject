from typing import Optional
from fastapi import FastAPI,HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class PC(BaseModel):
    id: int
    screen: Optional[str] = None
    keyboard: Optional[str] = None
    mouse: Optional[str] = None
    processor: Optional[str] = None
    video_card: Optional[str] = None


@app.get("/")
def get_ps():
    return repo