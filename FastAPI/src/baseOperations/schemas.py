from datetime import datetime, timezone
from pydantic import BaseModel, ConfigDict, Field, UUID4
    
class AddUser(BaseModel):
    email: str
    phone: int
    password: str
    firstname: str
    lastname: str

class User(AddUser):
    id: UUID4
    registrated_at: datetime