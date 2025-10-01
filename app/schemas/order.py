from datetime import date

from pydantic import BaseModel, Field

from app.schemas.car import CarResponse
from app.schemas.user import UserResponse


class OrderCreate(BaseModel):
    car_id: int
    order_date: date
    

class OrderResponse(BaseModel):
    id: int
    car: CarResponse
    user: UserResponse
    order_date: date

    class Config:
        from_attributes = True
    

class OrdersResponse(BaseModel):
    orders: list[OrderResponse] | None = None

    class Config:
        from_attributes = True
