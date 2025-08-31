from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.db.session import SessionLocal
from app.schemas.user import UserCreate
from app.services import user_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = user_service.register_user(db, user.username, user.password)
        return {"id": new_user.id, "username": new_user.username}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    result = user_service.authenticate_user(db, form_data.username, form_data.password)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result
