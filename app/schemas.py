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
    name: str = "Sebastian Valencia Zapata"
    position: str = "Fullstack developer"
    email: str = "sebastian.valencia@factored.ai"
    english: str = "B2"
    country: str = "Colombia"
    city: str = "Medellín"
    skills: dict = {
          "react": 4,
          "material-ui": 5,
          "python": 5,
          "fast-api": 3,
          "sql-alchemy": 3
        }

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Sebastian Valencia Zapata",
                    "position": "Fullstack developer",
                    "email": "sebastian.valencia@factored.ai",
                    "english": "B2",
                    "country": "Colombia",
                    "city": "Medellín",
                    "skills": {
                        "react": 4,
                        "material-ui": 5,
                        "python": 5,
                        "fast-api": 3,
                        "sql-alchemy": 3,
                    },
                },
            ]
        }
    }

