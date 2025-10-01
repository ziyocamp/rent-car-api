from enum import Enum
from typing import Annotated, List

from pydantic import BaseModel, PositiveFloat, PositiveInt, HttpUrl


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


class CarCreate(BaseModel):
    model: str
    brand: str
    price: PositiveFloat
    engine_type: Annotated[str, EngineType]
    doors: PositiveInt
    seats: PositiveInt
    fuel_type: Annotated[str, FuelType]
    air_condition: bool
    shape_type: Annotated[str, ShapeType]
    distance: PositiveInt
    images: List[HttpUrl]
    equipments: List[str]


class imageResponse(BaseModel):
    id: int
    url: HttpUrl

    class Config:
        from_attributes = True


class EquipmentResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class CarResponse(BaseModel):
    id: int
    model: str
    brand: str
    price: PositiveFloat
    engine_type: Annotated[str, EngineType]
    doors: PositiveInt
    seats: PositiveInt
    fuel_type: Annotated[str, FuelType]
    air_condition: bool
    shape_type: Annotated[str, ShapeType]
    distance: PositiveInt
    images: List[imageResponse] | None = None
    equipments: List[EquipmentResponse] | None = None

    class Config:
        from_attributes = True


class CarsReponse(BaseModel):
    cars: List[CarResponse] | None = None

    class Config:
        from_attributes = True


class CarUpdate:
    model: str
    brand: str
    price: PositiveFloat
    engine_type: Annotated[str, EngineType]
    doors: PositiveInt
    fuel_type: Annotated[str, FuelType]
    air_condition: bool
    shape_type: Annotated[str, ShapeType]
    distance: PositiveInt
