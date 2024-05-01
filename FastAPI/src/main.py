from typing import List
from fastapi import FastAPI, status, Request
from fastapi.encoders import jsonable_encoder
from fastapi_users import FastAPIUsers, fastapi_users
from pydantic import BaseModel, Field
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.add_author.router import router_operation

app = FastAPI(
    title='MyApp'
)

app.include_router(router_operation)
