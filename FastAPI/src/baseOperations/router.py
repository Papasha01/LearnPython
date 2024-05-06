from fastapi import APIRouter
from src.baseOperations.repository import BaseOperation
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
    users = await BaseOperation.findAllUsers()
    return {'status':200, "data": users, 'details':None}


@router_add_user.post('/')
async def add_user():
    # values = new_operation.model_dump()
    # stmt = insert(user).values(values)
    # await session.execute(stmt)
    # await session.commit()
    return {'status':200, 'data': 'Successfully add_user', 'description':None}