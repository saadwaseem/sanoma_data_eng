from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.models import User
from app.schemas import UserCreate
from app.logger import logger

def get_user(db: Session, id: int):
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        logger.warning(f"No user found with ID {id}")
        raise HTTPException(status_code=404, detail=f"No user found with ID {id}")

    logger.info(f"Retrieved user with ID {id}: {db_user.first_name} {db_user.last_name}")
    return db_user


def create_update_user(db: Session, user: UserCreate):
    logger.info(f"Received request to create or update user: {user.dict()}")

    db_user = db.query(User).filter(User.id == user.id).first()

    if db_user:
        logger.info(f"Updating existing user with ID {user.id}")
        for key, value in user.dict().items():
            if value is not None:
                setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        logger.info(f"User with ID {db_user.id} updated successfully.")
        return db_user.id

    logger.info(f"Creating a new user with ID {user.id}")
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logger.info(f"Successfully created new user with ID {new_user.id}")
    return new_user.id

def delete_user(db: Session, id: int):
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        logger.warning(f"Delete failed: No user found with ID {id}")
        raise HTTPException(status_code=404, detail=f"No user found with ID {id}")

    db.delete(db_user)
    db.commit()
    logger.info(f"User with ID {id} deleted successfully.")
    return {"message": f"User with ID {id} deleted"}
