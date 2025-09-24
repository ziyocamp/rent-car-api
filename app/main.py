from fastapi import FastAPI

from app.db import initial_db
from app.routers.users import router as user_router


app = FastAPI(title="Rent Car Api")

initial_db()

app.include_router(user_router)
