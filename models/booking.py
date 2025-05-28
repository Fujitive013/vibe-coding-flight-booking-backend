# Example booking data model
from pydantic import BaseModel
from typing import Optional


class BookingModel(BaseModel):
    user_id: str
    flight_id: str
    seat_number: Optional[int]
