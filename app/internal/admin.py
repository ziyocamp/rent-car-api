from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
import jwt

from app.dependencies import get_db
from app.models.user import User, UserRoles
from app.models.car import Car
from app.models.order import Order
from app.core.config import SECRET_KEY, JWT_ALGORITHM


router = APIRouter(
    prefix='/admin',
    tags=['Amin Endpoints']
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get('/')
async def get_cars(
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str, Depends(oauth2_scheme)]
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
    
    user_id = int(payload['sub'])

    user = db.query(User).filter_by(id=user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user does not exists.")
    elif user.role != UserRoles.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="permission denied.")

    total_users = db.query(User).count()
    total_cars = db.query(Car).count()
    total_orders = db.query(Order).count()

    return {
        "users": total_users,
        "cars": total_cars,
        "orders": total_orders
    }
