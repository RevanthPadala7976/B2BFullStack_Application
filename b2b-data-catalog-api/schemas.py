# schemas.py
from pydantic import BaseModel
from typing import List

class ProductBase(BaseModel):
    name: str
    category: str
    record_count: int
    fields: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode: True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode: True
