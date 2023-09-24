from fastapi import FastAPI
from functools import lru_cache
from . import models
from .database import engine
from .routers import post, user, auth, votes
from .config import Settings
from .config import settings


@lru_cache()
def get_settings():
    return Settings()


print(settings.database_port)

models.Base.metadata.create_all(bind=engine)  # This create all of our models

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)


# Default Route.
@app.get("/")
def root():
    return {"server": "Up and Running"}
