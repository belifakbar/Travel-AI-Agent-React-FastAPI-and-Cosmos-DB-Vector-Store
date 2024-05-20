from pydantic import BaseModel
from typing import List

# class Ship(BaseModel):
#     name: str
#     description: str
#     amenities: List[str]

class Incident(BaseModel):
    number: str
    description: str
    closenote: str
    state: str
    priority: str
    openedAt: str
    createdOn: str
    updatedOn: str

class Incidentmetadata(BaseModel):
    number: str
    openedAt: str
    createdOn: str
    updatedOn: str

# class Room(BaseModel):
#     name:str
#     price:str


# class Itinerary(BaseModel):
#     ShipID:str
#     Name:str
#     Rooms:List[str]
#     Schedule: List[str]
