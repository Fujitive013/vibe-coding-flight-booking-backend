from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from models import db
from schemas import UserCreate, UserLogin, UserOut

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def serialize_mongo_user(user):
    if user and "_id" in user:
        user["_id"] = str(user["_id"])
    return user


@router.post("/signup", response_model=UserOut)
async def signup(user: UserCreate):
    existing = await db.users.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_pw = pwd_context.hash(user.password)
    result = await db.users.insert_one({"email": user.email, "password": hashed_pw})
    user_out = await db.users.find_one({"_id": result.inserted_id})
    return serialize_mongo_user(user_out)


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db.users.find_one({"email": form_data.username})
    if not user or not pwd_context.verify(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"msg": "Login successful", "email": user["email"]}
