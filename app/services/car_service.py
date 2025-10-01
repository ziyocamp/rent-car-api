from typing import List

from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status

from app.models.car import Car, Image, Equipment
from app.schemas.car import CarCreate


def get_all_cars(db: Session) -> List[Car]:
    cars = db.query(Car).all()
    if cars is None:
        return []
    return cars

def get_one_car(db: Session, car_id: int) -> Car | None:
    car = db.query(Car).filter_by(id=car_id).first()

    if car:
        return car
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bunday Car mavjud emas.")

def create_car(db: Session, car_data: CarCreate) -> Car:
    car = Car(
        model=car_data.model,
        brand=car_data.brand,
        price=car_data.price,
        engine_type=car_data.engine_type,
        doors=car_data.doors,
        seats=car_data.seats,
        fuel_type=car_data.fuel_type,
        air_condition=car_data.air_condition,
        shape_type=car_data.shape_type,
        distance=car_data.distance
    )

    db.add(car)
    db.commit()
    db.refresh(car)

    equipments = [Equipment(name=name, car_id=car.id) for name in car_data.equipments]
    db.add_all(equipments)

    images = [Image(url=str(url), car_id=car.id) for url in car_data.images]
    db.add_all(images)

    db.commit()
    db.refresh(car)

    return car


def delete_car(db: Session, car_id: int) -> Car | None:
    car = db.query(Car).filter_by(id=car_id).first()

    if car:
        db.delete(car)
        db.commit()
        return {"msg": "o'chirildi"}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Car topilmadi.")

