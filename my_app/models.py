from sqlalchemy import Column, Integer, String

from .database import Base

class Objective(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    order = Column(Integer, index=True)