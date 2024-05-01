from fastapi import APIRouter, Depends
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from src.database import get_async_session

router_operation = APIRouter(
    prefix='/router_operation',
    tags=['Operation']
)

@router_operation.get('/')
async def get_op(session: AsyncSession = Depends(get_async_session)):
    q = f"select * from public.type_operation"
    result = await session.execute(q)
    return('result')