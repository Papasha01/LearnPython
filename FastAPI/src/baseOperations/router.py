from typing import Annotated
from fastapi import APIRouter, Depends
from src.baseOperations.repository import BaseOperation
from src.baseOperations.schemas import AddUser

router_get_user = APIRouter(
    prefix='/router_get_user',
    tags=['Get_user']
)

router_add_user = APIRouter(
    prefix='/router_add_user',
    tags=['Add_user']
)

@router_get_user.get('/')
async def get_users():
    result = await BaseOperation.findAllUsers()
    return {'status':200, "data": result, 'details':None}


@router_add_user.post('/')
async def add_user(
    data: Annotated[AddUser, Depends()]
):
    result = await BaseOperation.addUser(data)
    return {'status':200, 'data': result, 'description':None}