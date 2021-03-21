from typing import List, Optional

from pydantic import BaseModel


class ObjectiveBase(BaseModel):
    title: str
    order: int


class Objective(ObjectiveBase):
    id: int

    class Config:
        orm_mode = True