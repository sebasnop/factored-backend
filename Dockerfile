FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# The port where the backend will run
EXPOSE 8000

# Execute backend application
CMD ["python", "main.py"]