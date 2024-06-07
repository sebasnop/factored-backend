"""Module for creating pydantic models (as schemas)"""

from pydantic import BaseModel

class LoginSchema(BaseModel):
    """Login pydantic schema"""
    email: str
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "admin",
                    "password": "admin",
                },
                {
                    "email": "other",
                    "password": "other",
                }
            ]
        }
    }

class EmployeeSchema(BaseModel):
    """Employee pydantic schema"""
    name: str
    position: str
    email: str
    english: str
    country: str
    city: str
    skills: dict

