from fastapi import FastAPI
from .database import database, engine, metadata
from .api import auth, users

# Create tables
metadata.create_all(engine)

app = FastAPI(title="FastAPI JWT Auth")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include routers
app.include_router(auth.router, tags=["auth"])
app.include_router(users.router, tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI JWT Auth API"}
