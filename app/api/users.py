from fastapi import APIRouter, HTTPException, Depends
from ..core.deps import get_current_user
from ..core.security import get_password_hash
from ..schemas.user import User, UserCreate
from ..models.user import users
from ..database import database

router = APIRouter()

@router.post("/signup", response_model=User)
async def create_user(user: UserCreate):
    # Check if username already exists
    query = users.select().where(users.c.username == user.username)
    db_user = await database.fetch_one(query)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Create new user
    hashed_password = get_password_hash(user.password)
    query = users.insert().values(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    
    user_id = await database.execute(query)
    return {**user.dict(), "id": user_id}

@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {
        "message": f"Hello {current_user.username}, this is a protected route"
    }
