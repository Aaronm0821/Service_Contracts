from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db_setup import get_db

from apps.reps import crud
from pydantic_schemas import rep_schemas


router = APIRouter(tags=["Reps"])


@router.get("/reps", response_model=List[rep_schemas.Reps])
async def get_list_of_reps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reps = crud.get_list_of_reps(db, skip=skip, limit=limit)
    return reps


@router.post("/reps", response_model=rep_schemas.Reps)
async def add_rep(rep: rep_schemas.RepsCreate, db: Session = Depends(get_db)):
    return crud.add_rep(db=db, rep=rep)


@router.get("/reps/{rep_name}", response_model=rep_schemas.Reps)
async def get_rep_by_partial(name: str, db: Session = Depends(get_db)):
    db_rep_name = crud.get_rep_by_name(db, rep_name=name)

    if db_rep_name is None:
        raise HTTPException(status_code=404, detail="No reps found with this name")

    return db_rep_name


@router.delete("/reps/{id}")
async def delete_rep(rep_id: int, db: Session = Depends(get_db)):
    db_rep = crud.get_rep(db, rep_id)
    if db_rep is None:
        raise HTTPException(status_code=404, detail="No rep exists with this ID")
    return crud.remove_rep(db=db, rep_id=rep_id)




