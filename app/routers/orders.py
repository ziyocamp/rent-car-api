from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import Depends, Path
from sqlalchemy.orm import Session

from app.schemas.order import OrderResponse, OrderCreate, OrdersResponse
from app.dependencies import get_db
from app.services.order_service import create_order, get_all_orders, get_order


router = APIRouter(
    prefix='/orders',
    tags=['Orders Endpoints']
)


@router.get('/', response_model=OrdersResponse)
async def get_orders(db: Annotated[Session, Depends(get_db)]):
    return OrdersResponse(orders=get_all_orders(db))

@router.get('/{order_id}', response_model=OrderResponse)
async def get_one_order(order_id: Annotated[int, Path(gt=0)], db: Annotated[Session, Depends(get_db)]):
    return get_order(db, order_id)

@router.post('/', response_model=OrderResponse)
async def add_order(order_data: OrderCreate, db: Annotated[Session, Depends(get_db)]):
    return create_order(db, order_data)

