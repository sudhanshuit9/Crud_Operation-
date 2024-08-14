from typing import Union

from fastapi import FastAPI

from routes.index import User

app = FastAPI()

app.include_router(User)