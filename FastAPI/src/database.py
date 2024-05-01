from datetime import datetime, timezone
from typing import AsyncGenerator
from sqlalchemy import MetaData, Table, Column, Integer, Boolean, String, TIMESTAMP, ForeignKey, JSON, Uuid, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

metadata = MetaData()

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_async_engine(DB_URL, echo=True, future=True)

Base = declarative_base(bind=engine, future=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

book = Table(
    'book',
    metadata,
    Column('id',Integer,primary_key=True,autoincrement=True),
    Column('title', Integer, nullable=False),
    Column('user_id', Integer, ForeignKey('user.id'))
)

user = Table(
    'user',
    metadata,
    Column('id',Integer, primary_key=True, autoincrement=True),
    Column('first_name', String, nullable=False),
    Column('lastname', String, nullable=False),
    Column('email', String, nullable=False),
    Column('password', String, nullable=False),
    Column('registrated_at', TIMESTAMP, default=datetime.now(timezone.utc))
)
