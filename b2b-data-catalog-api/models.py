# models.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:rootPassword@localhost/b2b_data_catalog"

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)  # Example: Limit username to 50 characters
    password = Column(String(255))

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Example: Limit product name to 255 characters
    category = Column(String(100), index=True)  # Example: Limit category to 100 characters
    record_count = Column(Integer)
    fields = Column(String(255))  # Store fields as comma-separated string

class ProductSchema(BaseModel):
    id: int
    name: str
    category: str
    record_count: int
    fields: str

# Ensure tables are created in the database
Base.metadata.create_all(bind=engine)
