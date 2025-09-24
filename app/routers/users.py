from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user
from app.dependencies import get_db
from app.utils.email import send_verification_code_to_email

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user)

    await send_verification_code_to_email(new_user.email)

    return new_user
