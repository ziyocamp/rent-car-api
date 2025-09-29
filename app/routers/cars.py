from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import Depends, Path
from sqlalchemy.orm import Session

from app.schemas.car import CarResponse, CarsReponse, CarCreate, CarUpdate
from app.dependencies import get_db
from app.services.car_service import get_all_cars, get_one_car, create_car, delete_car


router = APIRouter(
    prefix='/cars',
    tags=['Cars Endpoints']
)


@router.get('/', response_model=CarsReponse)
async def get_cars(db: Annotated[Session, Depends(get_db)]):
    return CarsReponse(cars=get_all_cars(db))

@router.get('/{car_id}', response_model=CarResponse)
async def get_one_cars(car_id: Annotated[int, Path(gt=0)], db: Annotated[Session, Depends(get_db)]):
    return get_one_car(db, car_id)

@router.post('/', response_model=CarResponse)
async def add_car(car_data: CarCreate, db: Annotated[Session, Depends(get_db)]):
    car = create_car(db, car_data)

    return car

@router.delete('/{car_id}')
async def delete_cars(car_id: int, db: Annotated[Session, Depends(get_db)]):
    delete_car(db, car_id)

