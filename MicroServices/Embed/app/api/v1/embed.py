from fastapi import APIRouter
from fastapi import UploadFile, File, Depends, Body, Form
from typing import List
from sqlalchemy.orm import Session
from app.database.init import get_db
import app.controllers.embedCtrl as embedCtrl
# import app.validator.skill as skill_validator


router = APIRouter(
    tags=["Embedding"],
    prefix="/embed/api/v1"
)



@router.post("/", description="Create Embedding")
async def create_embedding(topic_name: str = Form(...),
                        files: List[UploadFile] = File(...), 
                        db:Session = Depends(get_db)):
    return embedCtrl.create_embedding(db, topic_name, files)

# @router.delete("/{skill_id}", description="Delete Skill")
# async def delete_skill():
#     return "Delete Created.."

# @router.put("/{skill_id}", description="Update Skill")
# async def update_skill():
#     return "Update skill."

# @router.get("/{skill_id}", description="Get Skill")
# async def get_skill(skill_id: str):
#     return "get skill."

# @router.get("/", description="List Skill")
# async def list_skill(skill_id: str):
#     return "List skill."
