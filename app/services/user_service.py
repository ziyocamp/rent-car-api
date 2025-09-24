from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status

from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.utils.password import get_hash_password


def create_user(db: Session, user: UserCreate) -> UserResponse:
    if db.query(User).filter_by(email=user.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="this user is already exists.")
    
    new_user = User(
        email=user.email,
        hash_password=get_hash_password(user.password),
        name=user.name,
        phone=user.phone
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
