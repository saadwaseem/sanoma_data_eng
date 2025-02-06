FROM python:3.9-slim

# Keep the image light
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /rest_api

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy relevant files only (without the dataset)
COPY app ./app
COPY static ./static

COPY docker-start.sh .
COPY database_setup.py .

# Expose FastAPI port
EXPOSE 8000

# Default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
