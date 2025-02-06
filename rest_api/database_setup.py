import json
from sqlalchemy.orm import Session
from app.database import engine, init_db, SessionLocal
from app.models import User

# Initialize the database schema
init_db()

# Ingest data from JSON
def load_data():
    with open("dataset/data.json", "r") as f:
        data = json.load(f)
    with Session(engine) as db:
        for record in data:
            user = User(**record)
            db.add(user)
        db.commit()
        print(f"{len(data)} records inserted.")

if __name__ == "__main__":
    load_data()
