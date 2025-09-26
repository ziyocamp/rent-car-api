from enum import Enum
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from app.db.database import Base


class EngineType(Enum):
    MECHANIC = "mechanic"
    AUTOMAT = "automat"


class FuelType(Enum):
    PETROL = "petrol"
    DIESEL = "diesel"
    ELECTRIC = "electric"
    HYBRID = "hybrid"


class ShapeType(Enum):
    SEDAN = "sedan"
    SUV = "suv"
    HATCHBACK = "hatchback"
    COUPE = "coupe"
    PICKUP = "pickup"


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    engine_type = Column(SQLEnum(EngineType), nullable=False)
    doors = Column(Integer, nullable=False)
    seats = Column(Integer, nullable=False)
    fuel_type = Column(SQLEnum(FuelType), nullable=False)
    air_condition = Column(Boolean, default=True)
    shape_type = Column(SQLEnum(ShapeType), nullable=False)
    distance = Column(Integer, nullable=False)  # masofa (km)
    is_available = Column(Boolean, default=True)

    # relationships
    images = relationship("Image", back_populates="car", cascade="all, delete")
    equipments = relationship("Equipment", back_populates="car", cascade="all, delete")
    

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)

    car_id = Column(Integer, ForeignKey("cars.id", ondelete="CASCADE"))
    car = relationship("Car", back_populates="images")


class Equipment(Base):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    car_id = Column(Integer, ForeignKey("cars.id", ondelete="CASCADE"))
    car = relationship("Car", back_populates="equipments")

