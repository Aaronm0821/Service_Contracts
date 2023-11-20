from sqlalchemy.orm import Session

from models import models
from pydantic_schemas import rep_schemas


def get_rep(db: Session, rep_id: int):
    return db.query(models.Reps).filter(models.Reps.id == rep_id).first()


def get_list_of_reps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reps).order_by(models.Reps.id).offset(skip).limit(limit).all()


def add_rep(db: Session, rep: rep_schemas.RepsCreate):
    db_rep = models.Reps(
        rep_first_name=rep.rep_first_name,
        rep_last_name=rep.rep_last_name,
        rep_email=rep.rep_email
    )
    db.add(db_rep)
    db.commit()
    db.refresh(db_rep)
    return db_rep


def remove_rep(db: Session, rep_id: int):
    db_rep = db.query(models.Reps).filter(models.Reps.id == rep_id).first()
    db.delete(db_rep)
    db.commit()


def get_customers_by_rep(db: Session, rep_id: int):
    return db.query(models.Customer).where(models.Customer.rep_id == rep_id).all()

def get_rep_by_name(db: Session, rep_name: str):
    return db.query(models.Reps).filter(models.Reps.rep_first_name == rep_name).first()








