"""Creating the database models."""

from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Employee(Base):
    """Employee SQL table model."""

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    position = Column(String)
    email = Column(String, unique=True, index=True)
    english = Column(String)
    country = Column(String)
    city = Column(String)
    skills = Column(JSON)
