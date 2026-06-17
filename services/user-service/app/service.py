from sqlalchemy.orm import Session
from app import repository, schemas

def add_user(db: Session, data: schemas.UserCreate) -> schemas.UserOut:
    user = repository.create_user(db, data)
    return schemas.UserOut.model_validate(user)

def fetch_user(db: Session, user_id: str) -> schemas.UserOut:
    user = repository.get_user(db, user_id)
    if user is None:
        raise ValueError("User not found")
    return schemas.UserOut.model_validate(user)

def fetch_all_users(db: Session, limit: int = 20, offset: int = 0) -> schemas.UserList:
    users = repository.get_users(db)
    total = len(users)
    items = [schemas.UserOut.model_validate(u) for u in users[offset:offset + limit]]
    return schemas.UserList(items=items, total=total, limit=limit, offset=offset)

def create_new_user(db: Session, data: schemas.UserCreate) -> schemas.UserOut:
    return add_user(db, data)

def get_all_users(db: Session, limit: int = 20, offset: int = 0) -> schemas.UserList:
    return fetch_all_users(db, limit=limit, offset=offset)

def get_user_by_id(db: Session, user_id: str) -> schemas.UserOut:
    return fetch_user(db, user_id)
