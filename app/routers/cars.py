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
    return CarsReponse(cars=get_all_cars(db))

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
