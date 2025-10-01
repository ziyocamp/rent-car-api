from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import Depends, Path
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
import jwt

from app.schemas.order import OrderResponse, OrderCreate, OrdersResponse
from app.dependencies import get_db
from app.services.order_service import create_order, get_all_orders, get_order
from app.core.config import SECRET_KEY, JWT_ALGORITHM

router = APIRouter(
    prefix='/orders',
    tags=['Orders Endpoints']
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get('/', response_model=OrdersResponse)
async def get_orders(db: Annotated[Session, Depends(get_db)]):
    return OrdersResponse(orders=get_all_orders(db))

@router.get('/{order_id}', response_model=OrderResponse)
async def get_one_order(order_id: Annotated[int, Path(gt=0)], db: Annotated[Session, Depends(get_db)]):
    return get_order(db, order_id)

@router.post('/', response_model=OrderResponse)
async def add_order(
    order_data: OrderCreate, 
    db: Annotated[Session, Depends(get_db)], 
    token: Annotated[str, Depends(oauth2_scheme)]
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])

    user_id = int(payload['sub'])

    return create_order(db, order_data, user_id)

