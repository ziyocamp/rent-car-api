from fastapi import FastAPI
from app.db import initial_db

app = FastAPI(title="Rent Car Api")

initial_db()
