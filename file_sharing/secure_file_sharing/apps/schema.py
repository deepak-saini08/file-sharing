
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class FileOut(BaseModel):
    id: int
    filename: str
    uploaded_at: str

    class Config:
        orm_mode = True
