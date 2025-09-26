from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas.car import CarResponse, CarsReponse, CarCreate, CarUpdate
from app.dependencies import get_db
from app.services.car_service import get_all_cars


router = APIRouter(
    prefix='/cars',
    tags=['Cars Endpoints']
)


@router.get('/', response_model=CarsReponse)
async def get_cars(db: Annotated[Session, Depends(get_db)]):
    cars = []
    for car in get_all_cars(db):
        images = []
        for image in car.images:
            images.append(image.url)
        equipments = []
        for equipment in car.equipments:
            equipments.append(equipment.name)
            
        cars.append(CarResponse(
            id=car.id,
            model=car.model,
            brand=car.brand,
            price=car.price,
            engine_type=car.engine_type,
            doors=car.doors,
            seats=car.seats,
            fuel_type=car.fuel_type,
            air_condition=car.air_condition,
            shape_type=car.shape_type,
            distance=car.distance,
            images=images,
            equipments=equipments
        ))

    result = CarsReponse(
        cars=cars
    )

    return result

# @router.get('/{car_id}') # , response_model=CarResponse
# async def get_one_cars(car_id: int, db: Annotated[Session, Depends(get_db)]):
#     pass

# @router.post('/') # , response_model=CarResponse
# async def add_car(car_data: CarCreate, db: Annotated[Session, Depends(get_db)]):
#     pass

# @router.put('/{car_id}') # , response_model=CarResponse
# async def update_cars(car_id: int, car_data: CarUpdate, db: Annotated[Session, Depends(get_db)]):
#     pass


# @router.delete('/{car_id}')
# async def delete_cars(car_id: int, db: Annotated[Session, Depends(get_db)]):
#     pass
