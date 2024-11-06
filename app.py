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

repo: List[PC] = [
    PC(id=1, screen="24 inch Full HD", 
       keyboard="Mechanical", 
       mouse="Optical", 
       processor="Intel i5-10400",
       video_card="NVIDIA GTX 1660")
]

@app.get("/pc", response_model=List[PC])
def get_ps():
    return repo
@app.get("/pc/{id}",response_model=PC)
def find_pc(id:int):
    pc = next((pc for pc in repo if pc.id == id ),None)
    if pc is None:
        raise HTTPException(status_code=404,detail = "PC not found")
    return pc
@app.post("/pc",response_model=PC)
def create_pc(pc:PC):
    repo.append(pc)
    return pc
@app.put("/pc",response_model=PC)
def update_pc(pc:PC):
    for i in repo:
        if i.id == pc.id:
            if pc.screen is not None:
                i.screen = pc.screen
            if pc.keyboard is not None:
                i.keyboard = pc.keyboard
            if pc.mouse is not None:
                i.mouse = pc.mouse
            if pc.processor is not None:
                i.processor = pc.processor
            if pc.video_card is not None:
                i.video_card = pc.video_card
            return i
    raise HTTPException(status_code=404,detail = "PC not pound")
@app.delete("/pc/{id}",status_code=204)
def delete_pc(id:int):
    global repo 
    repo = [pc for pc in repo if pc.id != id]
    return