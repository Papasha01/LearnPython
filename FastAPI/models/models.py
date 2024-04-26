from datetime import datetime, timezone
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

books = Table(
    'books',
    metadata,
    Column('id',Integer,primary_key=True),
    #Column('author', String, nullable=False),
    Column('title', Integer, nullable=False)
)

authors = Table(
    'author',
    metadata,
    Column('id',Integer,primary_key=True),
    Column('name', String, nullable=False),
    Column('lastname', String, nullable=False),
    Column('birthday', TIMESTAMP, nullable=False),
    Column('registrated_at', TIMESTAMP, default=datetime.now(timezone.utc)),
    Column('book_id', Integer, ForeignKey('books.id'))
)