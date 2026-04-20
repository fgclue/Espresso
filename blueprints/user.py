from flask import Blueprint
from typing import Optional, List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import Base, db
from decimal import *

user = Blueprint('user', __name__, url_prefix="/user")
role = Blueprint('role', __name__, url_prefix="/role")

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(1024))
    email: Mapped[Optional[str]] = mapped_column(String(256))
    password: Mapped[str] = mapped_column(String(1024))
    unsafekey: Mapped[Optional[str]] = mapped_column(String(1024))

    roles: Mapped[List["Role"]] = relationship()

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r}, password={self.password!r}, unsafekey={self.unsafekey!r})"

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(1024))

    permissions: Mapped[List["Permission"]] = relationship()

    def __repr__(self) -> str:
        return f"Role(id={self.id!r}, name={self.name!r})"

class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(1024))

    def __repr__(self) -> str:
        return f"Permission(id={self.id!r}, name={self.name!r})"

"""

user -> id, email, name, password, role, fiscal barcode (optional)
item:        get, patch, put, delete
user:        get, patch, put, delete
roles:       get, patch, put, delete
transaction: get, patch, put, delete
"""