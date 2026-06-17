from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate

def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=user.hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
