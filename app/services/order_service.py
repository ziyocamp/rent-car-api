from typing import List

from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status

from app.models.order import Order
from app.models.user import User
from app.models.car import Car
from app.schemas.order import OrderCreate, OrderResponse


def create_order(db: Session, order_data: OrderCreate, user_id: int):

    user = db.query(User).filter_by(id=user_id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bunday user mavjud emas.")
    
    car = db.query(Car).filter_by(id=order_data.car_id).first()

    if car is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bunday car mavjud emas.")
        
    order = Order(
        user_id = user.id,
        car_id = car.id,
        order_date = order_data.order_date
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order

def get_all_orders(db: Session):
    orders = db.query(Order).all()

    if orders is None:
        return []
    
    return orders

def get_order(db: Session, order_id: int):
    order = db.query(Order).filter_by(id=order_id).first()

    if order:
        return order
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bunday Order mavjud emas.")
