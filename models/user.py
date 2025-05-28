# Example user data model (ODM/ORM or helper)
from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    email: EmailStr
    hashed_password: str
