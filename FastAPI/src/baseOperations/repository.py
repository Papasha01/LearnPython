from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import new_session, user
from src.baseOperations.schemas import User
from sqlalchemy import insert, select, delete, update
from fastapi.encoders import jsonable_encoder
import json

class BaseOperation:
    @classmethod
    async def findAllUsers(cls) -> list[User]:
        async with new_session() as session:
            q = select(user)
            result = await session.execute(q)
            # for i in result.all():
            #     for j in i:
            #         print(type(j))
            user_schemas = [User.model_validate(user, from_attributes=True) for user in result.all()]
            return user_schemas
        