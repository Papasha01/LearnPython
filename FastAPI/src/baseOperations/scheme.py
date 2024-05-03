from datetime import datetime, timezone
from pydantic import BaseModel, Field, UUID4
    
class Product(BaseModel):
    id: int 
    name: str   
    price: float   
    descriprion: str   

class Order (BaseModel):
    id: int
    user_id: int
    product_id: int
    count: int
    date: datetime

class User(BaseModel):
    id: UUID4
    email: str
    phone: int
    password: str
    firstname: str
    lastname: str
    registrated_at: datetime

class AddUser(BaseModel):
    email: str = 'test@gmail.com'
    phone: int = 79123456789
    password: str = 'ReallyHardPass'
    firstname: str = 'Elon'
    lastname: str = 'Mask'