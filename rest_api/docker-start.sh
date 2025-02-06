#!/bin/sh

if [ ! -d "db" ]; then
  echo "Creating db directory..."
  mkdir db
else
  echo "db directory already exists."
fi

if [ ! -f "db/test.db" ]; then
  echo "Creating test.db file..."
  touch db/test.db
  # Run database migrations and ingest data only once
  python database_setup.py
else
  echo "test.db file already exists."
fi

# Start FastAPI server
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
