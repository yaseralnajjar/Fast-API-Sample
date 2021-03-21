from fastapi import Depends, FastAPI, HTTPException

from . import crud, models, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/objectives/")
def read_objectives(db: Session = Depends(get_db)):
    return db.query(models.Objective).all()


@app.post("/objectives/")
def create_objective(objective: schemas.ObjectiveBase, db: Session = Depends(get_db)):
    print("qqqqqqqqqqqqqqq")
    test = crud.create_objective(db=db, objective=objective)
    print(test)
    return test


@app.put("/objectives/{objective_id}")
def update_objective(objective_id: int, objective: schemas.ObjectiveBase, db: Session = Depends(get_db)):
    db_objective = crud.update_objective(db, objective_id=objective_id, objective=objective)
    if db_objective:
        return db_objective
    else:
        raise HTTPException(status_code=404, detail="Objective not found")


@app.delete("/objectives/{objective_id}")
def update_objective(objective_id: int, db: Session = Depends(get_db)):
    db_objective = crud.delete_objective(db, objective_id=objective_id)
    if db_objective:
        return db_objective
    else:
        raise HTTPException(status_code=404, detail="Objective not found")