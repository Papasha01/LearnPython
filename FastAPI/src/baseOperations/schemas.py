from datetime import datetime, timezone
from pydantic import BaseModel, ConfigDict, Field, UUID4
    
class User(BaseModel):
    id: UUID4
    email: str
    phone: int
    password: str
    firstname: str
    lastname: str
    registrated_at: datetime

# class User(AddUser):
    
