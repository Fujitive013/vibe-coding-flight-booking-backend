from fastapi import APIRouter, HTTPException
from models import db
from schemas import FlightCreate, FlightOut
from bson import ObjectId

router = APIRouter()


@router.post("/flights", response_model=FlightOut)
async def create_flight(flight: FlightCreate):
    result = await db.flights.insert_one(flight.dict())
    new_flight = await db.flights.find_one({"_id": result.inserted_id})
    return new_flight


@router.get("/flights", response_model=list[FlightOut])
async def list_flights():
    flights = await db.flights.find().to_list(100)
    return flights
