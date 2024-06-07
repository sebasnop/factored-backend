from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Employee
from app.schemas import EmployeeSchema, LoginSchema

app = FastAPI()

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


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.post("/login", status_code=status.HTTP_200_OK, tags=["user"])
async def login(user_credentials: LoginSchema):
    """Login endpoint"""

    email = user_credentials.email
    password = user_credentials.password

    if email == "admin" and password == "admin":
        return {"message": "Login successful"}
    return JSONResponse(
        content={"message": "User not authorized."},
        status_code=status.HTTP_401_UNAUTHORIZED
        )


@app.get("/employees", response_model=list[EmployeeSchema], tags=["employees"])
async def get_employees(db: Session = Depends(get_db)):
    """GET employees endpoint"""
    employees = db.query(Employee).all()
    return employees

@app.get("/employees/{employee_id}", response_model=EmployeeSchema, tags=["employees"])
async def get_employee(employee_id: int, db: Session = Depends(get_db)):
    """GET an employee endpoint"""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return employee


@app.post("/employees", tags=["employees"])
async def create_employee(employee_data: EmployeeSchema, db: Session = Depends(get_db)):
    """POST an employee endpoint"""
    new_employee = Employee(**employee_data.dict())
    db.add(new_employee)
    print("C")
    try:
        db.commit()
        return new_employee
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST) from e

