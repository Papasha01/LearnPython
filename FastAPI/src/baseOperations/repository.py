from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import new_session, user
from src.baseOperations.schemas import User, AddUser
from sqlalchemy import insert, select, delete, update

class BaseOperation:
    @classmethod
    async def findAllUsers(cls) -> list[User]:
        async with new_session() as session:
            q = select(user)
            result = await session.execute(q)
            user_schemas = [User.model_validate(user, from_attributes=True) for user in result.all()]
            return user_schemas

    @classmethod
    async def addUser(cls, new_data:AddUser) -> list[User]:
        async with new_session() as session:
            values = new_data.model_dump()
            q = insert(user).values(values)            
            await session.execute(q)
            await session.commit()
            return 'User has been added!'