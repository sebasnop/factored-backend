"""Module to CRUD directly to the database."""

import logging

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException, status

from app.schemas import EmployeeSchema
from app.models import Employee

# Configura el logger
logger = logging.getLogger(__name__)


def create_employee(db: Session, employee: EmployeeSchema):
    """Create employee into database"""
    new_employee = Employee(**employee.dict())
    try:
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee
    except IntegrityError as e:
        db.rollback()
        logger.error("IntegrityError: %s", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Integrity error, probably a duplicate entry."
        ) from e
    except SQLAlchemyError as e:
        db.rollback()
        logger.error("SQLAlchemyError: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your request."
        ) from e
    except Exception as e:
        db.rollback()
        logger.error("Unexpected error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        ) from e


def read_employee(db: Session, employee_id: int):
    """Get one employee from database by its id value"""
    return db.query(Employee).filter(Employee.id == employee_id).first()


def read_employees(db: Session, skip: int = 0, limit: int = 100):
    """Get employees from database"""
    return db.query(Employee).offset(skip).limit(limit).all()


def delete_employee(db: Session, employee_id: int):
    """Delete one employee from database by its id value"""
    employee = read_employee(db=db, employee_id=employee_id)
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    employee_copy = employee
    db.delete(employee)
    db.commit()
    return employee_copy
