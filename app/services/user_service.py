from sqlalchemy.orm import Session
from app.crud import user as crud_user
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User

def register_user(db: Session, username: str, password: str) -> User:
    existing = crud_user.get_user_by_username(db, username)
    if existing:
        raise ValueError("Username already exists")
    hashed_pw = hash_password(password)
    return crud_user.create_user(db, username, hashed_pw)

def authenticate_user(db: Session, username: str, password: str):
    user = crud_user.get_user_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
 
