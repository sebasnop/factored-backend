"""Module for creating pydantic models (as schemas)"""

from pydantic import BaseModel

defaultName: str = "Sebastian Valencia Zapata"
defaultPosition: str = "Fullstack developer"
defaultEmail: str = "sebastian.valencia@factored.ai"
defaultEnglish: str = "B2"
defaultCountry: str = "Colombia"
defaultCity: str = "Medellín"
defaultSkills: dict = {
    "Frontend": 4,
    "Backend": 3,
    "Cloud": 3,
    "IA": 3,
    "Analytics": 3
}

class LoginSchema(BaseModel):
    """Login pydantic schema"""
    email: str
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "admin@factored.ai",
                    "password": "admin",
                },
            ]
        }
    }

class EmployeeSchema(BaseModel):
    """Employee pydantic schema"""
    name: str = defaultName
    position: str = defaultPosition
    email: str = defaultEmail
    english: str = defaultEnglish
    country: str = defaultCountry
    city: str = defaultCity
    skills: dict = defaultSkills

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": defaultName,
                    "position": defaultPosition,
                    "email": defaultEmail,
                    "english": defaultEnglish,
                    "country": defaultCountry,
                    "city": defaultCity,
                    "skills": defaultSkills
                },
            ]
        }
    }

class EmployeeIdSchema(BaseModel):
    """Employee pydantic schema with id attribute"""
    id: int
    name: str = defaultName
    position: str = defaultPosition
    email: str = defaultEmail
    english: str = defaultEnglish
    country: str = defaultCountry
    city: str = defaultCity
    skills: dict = defaultSkills

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": defaultName,
                    "position": defaultPosition,
                    "email": defaultEmail,
                    "english": defaultEnglish,
                    "country": defaultCountry,
                    "city": defaultCity,
                    "skills": defaultSkills
                },
            ]
        }
    }
