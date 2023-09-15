from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models
from database import SessionLocal

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_new_user(user: models.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login/")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    if not user.password == password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {"status": "Logged in successfully!"}
