from enum import Enum

from sqlalchemy import Column, Integer, String, Boolean, Enum as SQLEnum

from app.db.database import Base


class UserRoles(Enum):
    user = "user"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hash_password = Column(String, nullable=False)
    phone = Column(String)
    name = Column(String)
    is_verified = Column(Boolean, default=False)
    role = Column(SQLEnum(UserRoles), default=UserRoles.user)

    def __repr__(self) -> str:
        return f"User(id={self.id}, email={self.email}, name={self.name}, phone={self.phone})"
