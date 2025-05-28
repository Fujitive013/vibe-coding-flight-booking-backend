from fastapi import APIRouter, HTTPException
from models import db
from schemas import BookingCreate, BookingOut
from bson import ObjectId

router = APIRouter()


@router.post("/bookings", response_model=BookingOut)
async def create_booking(booking: BookingCreate):
    result = await db.bookings.insert_one(booking.dict())
    new_booking = await db.bookings.find_one({"_id": result.inserted_id})
    return new_booking


@router.get("/bookings", response_model=list[BookingOut])
async def list_bookings():
    bookings = await db.bookings.find().to_list(100)
    return bookings
