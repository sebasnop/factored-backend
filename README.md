# Backend for Factored Employees

This repository contains the backend for Factored Employees app.

This backend was build using `FastAPI` and `SQLAlchemy` for ORM.

Also, it is used `uvicorn` to run this backend.

The entry point or running the project is `main.py`.

## Endpoints

As you can see on `app/api.py`, the application have the next endpoints:

- `/login/`: Basic user authentication.
- `/employees/`: Getting all employees from database.
- `/create_employee/`: Creating a new employee into database.
- `/employees/{employee_id}`: Getting an employee by its id.
- `/delete_employee/{employee_id}`: Deleting an employee by its id.

## Docker

The `Docekfile` in this repository will let you to run the project easily.

The `requirements.txt` provide the neccesary packages that Docker use to build its image.

## Author

This project was made by Sebastian Valencia Zapata as part of [Factored](https://factored.ai/) assessment.
