from sqlalchemy import MetaData, Table, Column, Integer, Boolean, String, TIMESTAMP, ForeignKey, JSON, Uuid, UUID

metadata = MetaData()

type_operation = Table(
    'type_operation',
    metadata,
    Column('id',Integer,primary_key=True, autoincrement=True),
    Column('name',String)
)

operation = Table(
    'operation',
    metadata,
    Column('id',Integer,primary_key=True, autoincrement=True),
    Column('title', Integer, nullable=False),
    Column('count', Integer),
    Column('type_operation_id', Integer, ForeignKey(type_operation.c.id))
)

