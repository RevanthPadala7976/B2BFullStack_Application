
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing import List
import models
import schemas
from models import User, Product, SessionLocal, engine

# Configuration for JWT
SECRET_KEY = "1706f5dcaca5f94c59f520e00d0bb6b8df42b56b1942885c61362b7a5f9ecd9e"
ALGORITHM = "HS256"

# Create all database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# CORS settings
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependancy to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Authenticate user credentials
def authenticate_user(db, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and pwd_context.verify(password, user.password):
        return user
    return False

# Create JWT token
def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

default_users = [
    {"username": "admin", "password": "admin@123"},
    {"username": "user1", "password": "user@123"},
    {"username":"user2", "password":"user"}
]

default_products = [
    {"name": "Product A", "category": "Category 1", "record_count": 100, "fields": "field1, field2, field3"},
    {"name": "Product B", "category": "Category 2", "record_count": 50, "fields": "field4, field5"},
    {"name": "Product C", "category": "Category 1", "record_count": 200, "fields": "field6, field7, field8"},
]

def create_default_data(db: Session):
    for user_data in default_users:
        existing_user = db.query(User).filter(User.username == user_data["username"]).first()
        if not existing_user:
            hashed_password = pwd_context.hash(user_data["password"])
            db_user = User(username=user_data["username"], password=hashed_password)
            db.add(db_user)
    for product_data in default_products:
        existing_product = db.query(Product).filter(Product.name == product_data["name"]).first()
        if not existing_product:
            db_product = Product(**product_data)
            db.add(db_product)
    db.commit()

@app.on_event("startup")
async def startup_event():
    db = SessionLocal()
    create_default_data(db)
    db.close()

# Login endpoint to authenticate user and return token
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint to get list of products (required authentication)
@app.get("/products", response_model=List[schemas.Product])
async def read_products(skip: int = 0, limit: int = 10, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

# Endpoint to get product details by ID (requires authentication)
@app.get("/products/{product_id}", response_model=schemas.Product)
async def read_product(product_id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
