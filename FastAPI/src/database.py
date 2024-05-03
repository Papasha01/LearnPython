from datetime import datetime, timezone
from typing import AsyncGenerator
from sqlalchemy import BigInteger, DateTime, Float, MetaData, Table, Column, Integer, Boolean, String, TIMESTAMP, ForeignKey, JSON, Uuid, UUID
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
import sqlalchemy as sa
metadata = MetaData()

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_async_engine(DB_URL, echo=True, future=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

user = Table(
    'user',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=sa.func.uuid_generate_v4()),
    Column('email', String, nullable=False),
    Column('phone', BigInteger, nullable=False, ),
    Column('password', String, nullable=False),
    Column('firstname', String(50), nullable=False),
    Column('lastname', String(50), nullable=False),
    Column('registrated_at', DateTime, server_default=sa.func.now(), nullable=False)
)

order= Table(
    'order',
    metadata,
    Column('id',Integer, primary_key=True, autoincrement=True),
    Column('user_id', UUID(as_uuid=True), ForeignKey('user.id'), nullable=False),
    Column('product_id', Integer, ForeignKey('product.id'), nullable=False),
    Column('count', Integer, nullable=False),
    Column('date', DateTime, server_default=sa.func.now(),nullable=False)
)

product= Table(
    'product',
    metadata,
    Column('id',Integer, primary_key=True, autoincrement=True),
    Column('name', String(50), nullable=False),
    Column('price', Float, nullable=False),
    Column('descriprion', String, nullable=False)
)