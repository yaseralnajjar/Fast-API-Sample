from sqlalchemy.orm import Session

from . import models, schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_objective(db: Session, objective: schemas.ObjectiveBase):
    db_objective = models.Objective(**objective.dict())
    db.add(db_objective)
    db.commit()
    db.refresh(db_objective)
    return db_objective


def update_objective(db: Session, objective_id: int, objective: schemas.ObjectiveBase):
    db_objective = db.query(models.Objective).filter(models.Objective.id == objective_id).first()
    db_objective.title = objective.title
    db_objective.order = objective.order
    db.commit()
    db.refresh(db_objective)
    return db_objective


def delete_objective(db: Session, objective_id: int):
    db_objective = db.query(models.Objective).filter(models.Objective.id == objective_id).delete()
    db.commit()
    return db_objective
