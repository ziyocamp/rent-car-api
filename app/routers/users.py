from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse, VerificationCode
from app.services.user_service import create_user
from app.dependencies import get_db
from app.utils.email import send_verification_code_to_email
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user)

    await send_verification_code_to_email(new_user.email, new_user.verification_code)

    return new_user

@router.post("/verify", response_model=UserResponse)
async def create_new_user(verification_data: VerificationCode, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=verification_data.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user does not exists.")
    
    if user.verification_code != verification_data.code:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid verification code.")
    
    user.is_verified = True
    db.commit()

    return user
