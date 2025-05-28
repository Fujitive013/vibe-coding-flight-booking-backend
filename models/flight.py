# Example flight data model
from pydantic import BaseModel


class FlightModel(BaseModel):
    flight_number: str
    origin: str
    destination: str
    departure_time: str
    arrival_time: str
    seats: int
