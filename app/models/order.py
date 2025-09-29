from sqlalchemy import Column, Integer, ForeignKey, Enum as SQLEnum, Date
from sqlalchemy.orm import relationship
from app.db.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    order_date = Column(Date)

    car = relationship("Car", back_populates="orders")
    user = relationship("User", back_populates="orders")
