from typing import List

from sqlalchemy.orm import Session

from app.models.car import Car


def get_all_cars(db: Session) -> List[Car]:
    cars = db.query(Car).all()
    if cars is None:
        return []
    return cars
