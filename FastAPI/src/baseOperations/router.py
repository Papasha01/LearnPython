from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from sqlalchemy import insert, select, delete, update
from src.baseOperations.scheme import User, Order, Product, AddUser
from src.database import user, product, order
from fastapi.encoders import jsonable_encoder

router_get_user = APIRouter(
    prefix='/router_get_user',
    tags=['Get_user']
)

router_add_user = APIRouter(
    prefix='/router_add_user',
    tags=['Add_user']
)

@router_get_user.get('/', response_model=List [User])
async def get_users(session: AsyncSession = Depends(get_async_session)):
    q = select(user)
    result = await session.execute(q)
    return result.all()

@router_add_user.post('/')
async def add_suser(new_operation: AddUser, session: AsyncSession = Depends(get_async_session)):
    values = new_operation.model_dump()
    stmt = insert(user).values(values)
    print(stmt)
    await session.execute(stmt)
    await session.commit()
    return {'status':200, 'data': 'Successfully add data', 'description':None}