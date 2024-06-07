"""API endpoints definition"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.schemas import LoginSchema, EmployeeSchema, EmployeeIdSchema

from app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    """Getting SQLAlchemy database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/login/", status_code=status.HTTP_200_OK, tags=["user"])
def login(user_credentials: LoginSchema):
    """Login endpoint"""
    email = user_credentials.email
    password = user_credentials.password

    if email == "admin" and password == "admin":
        return {"message": "Login successful"}
    return JSONResponse(
        content={"message": "User not authorized."},
        status_code=status.HTTP_401_UNAUTHORIZED
        )


@app.post("/create_employee/", response_model=EmployeeIdSchema,
status_code=status.HTTP_201_CREATED, tags=["employees"])
def create_employee(employee_data: EmployeeSchema, db: Session = Depends(get_db)):
    """POST endpoint for create employee"""
    return crud.create_employee(db=db, employee=employee_data)


@app.get("/employees/", response_model=list[EmployeeIdSchema],
status_code=status.HTTP_200_OK, tags=["employees"])
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """GET endpoint for read employees"""
    employees = crud.read_employees(db, skip=skip, limit=limit)
    return employees


@app.get("/employees/{employee_id}", response_model=EmployeeIdSchema,
status_code=status.HTTP_200_OK, tags=["employees"])
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    """GET endpoint for read one employee"""
    db_employee = crud.read_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return db_employee

@app.delete("/delete_employee/{employee_id}", response_model=EmployeeIdSchema,
status_code=status.HTTP_200_OK, tags=["employees"])
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """DELETE endpoint for delete one employee"""
    return crud.delete_employee(db, employee_id=employee_id)
