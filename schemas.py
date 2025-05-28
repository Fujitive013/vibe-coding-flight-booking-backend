from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: str = Field(..., alias="_id")
    email: EmailStr


class FlightCreate(BaseModel):
    flight_number: str
    origin: str
    destination: str
    departure_time: str
    arrival_time: str
    seats: int


class FlightOut(BaseModel):
    id: str = Field(..., alias="_id")
    flight_number: str
    origin: str
    destination: str
    departure_time: str
    arrival_time: str
    seats: int


class BookingCreate(BaseModel):
    user_id: str
    flight_id: str
    seat_number: Optional[int]


class BookingOut(BaseModel):
    id: str = Field(..., alias="_id")
    user_id: str
    flight_id: str
    seat_number: Optional[int]
