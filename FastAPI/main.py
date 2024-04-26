from typing import List
from fastapi import FastAPI, status, Request
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title='TestApp'
)

@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


users = [
    {'id':1, 'name':'Bob', 'lastname': 'Rogov'},
    {'id':2, 'name':['Alien'], 'lastname': 'Smirnov'},
    {'id':3, 'name':'Vicrot', 'lastname': 'Eremko'}
]

class User(BaseModel):
    id:int
    name:str = Field(max_length=50)
    lastname:str = Field(max_length=50)

@app.get("/user/{user_id}", response_model=List[User])
def user(user_id:int):
    return [n for n in users if n['id'] == user_id]

fake_traids = [
    {'id':1, 'user_id':1, 'currency': 'BTC', 'count':111, 'price':444},
    {'id':2, 'user_id':2, 'currency': 'ETH', 'count':222, 'price':555},
    {'id':3, 'user_id':3, 'currency': 'CWD', 'count':333, 'price':666}
]

@app.get("/traids")
def traids(limit:int = 1, offset:int=0):
    return fake_traids[offset:][:limit]

@app.post("/user/{user_id}")
def change_user_name(user_id: int, new_name:str):
    cur_user = list(filter(lambda user:user['id']==user_id, users))[0]
    
    cur_user['name'] = new_name
    return {'status':200, 'data':cur_user}

class Traid(BaseModel):
    id:int
    user_id:int
    currency:str = Field(max_length=10)
    count:int
    price:int = Field(ge=0)

@app.post("/traids")
def add_traids(traids:List[Traid]):
    fake_traids.extend(traids)
    return {'status':200, 'data':fake_traids}
    