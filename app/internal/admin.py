from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import Depends, Path
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
import jwt

from app.dependencies import get_db
from app.models.user import User
from app.models.car import Car
from app.models.order import Order
from app.core.config import SECRET_KEY, JWT_ALGORITHM


router = APIRouter(
    prefix='/amin',
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
    role = int(payload['role'])

    user = db.query(User).filter_by(id=user_id).first()
    if user is None:
        raise 
    elif user.role != role:
        raise

    total_users = db.query(User).count()
    total_cars = db.query(Car).count()
    total_orders = db.query(Order).count()

    return {
        "users": total_users,
        "cars": total_cars,
        "orders": total_orders
    }
