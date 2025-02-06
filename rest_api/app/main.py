from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app import models, schemas, crud, auth
from app.database import engine, SessionLocal
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI(title="Register API")

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Exception Handlers
@app.exception_handler(SQLAlchemyError)
async def handle_database_exceptions(request: Request, exc: SQLAlchemyError):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Database error occurred",
            "path": request.url.path
        }
    )

@app.exception_handler(HTTPException)
async def handle_http_exceptions(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "path": request.url.path}
    )

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routes
@app.get("/favicon.ico", response_class=FileResponse)
async def favicon():
    return FileResponse("static/favicon.ico")

@app.get("/user/{id}", response_model=schemas.UserResponse, dependencies=[Depends(auth.verify_api_key)])
def get_user(id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, id)
    return user

@app.post("/user", response_model=int, dependencies=[Depends(auth.verify_api_key)])
def create_update_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_id = crud.create_update_user(db, user)
    return user_id

@app.delete("/user/{id}", dependencies=[Depends(auth.verify_api_key)])
def delete_user(id: int, db: Session = Depends(get_db)):
    response_msg = crud.delete_user(db, id)
    return response_msg
