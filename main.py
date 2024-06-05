"""Module to start running the backend service with FastAPI."""

from fastapi import FastAPI, HTTPException

from .database import SessionLocal #, engine

app = FastAPI()

# Dependency
def get_db():
    """Getting SQLAlchemy database."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login")
async def login(username: str, password: str):
    """Login POST request validation."""
    if username == "admin" and password == "admin":
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
