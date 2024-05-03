from fastapi import FastAPI
from src.baseOperations.router import router_get_user, router_add_user

app = FastAPI(
    title='MyApp'
)

app.include_router(router_get_user)
app.include_router(router_add_user)
