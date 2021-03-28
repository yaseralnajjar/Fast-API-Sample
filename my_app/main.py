from fastapi import Depends, FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/objectives/")
def get_objectives(db: Session = Depends(get_db)):
    return db.query(models.Objective).all()


@app.post("/objectives/")
def create_objective(objective: schemas.ObjectiveBase, db: Session = Depends(get_db)):
    db_objective = crud.create_objective(db=db, objective=objective)
    return db_objective


@app.put("/objectives/{objective_id}")
def update_objective(objective_id: int, objective: schemas.ObjectiveBase, db: Session = Depends(get_db)):
    db_objective = crud.update_objective(db, objective_id=objective_id, objective=objective)
    if db_objective:
        return db_objective
    else:
        raise HTTPException(status_code=404, detail="Objective not found")


@app.delete("/objectives/{objective_id}")
def delete_objective(objective_id: int, db: Session = Depends(get_db)):
    db_objective = crud.delete_objective(db, objective_id=objective_id)
    if db_objective:
        return db_objective
    else:
        raise HTTPException(status_code=404, detail="Objective not found")