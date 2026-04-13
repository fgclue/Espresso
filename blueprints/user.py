from flask import Blueprint, request
from typing import Optional
from sqlalchemy import String, Numeric
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Mapped, mapped_column
from models import Base, db
from decimal import *

user = Blueprint('user', __name__, url_prefix="/user")

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(1024))
    email: Mapped[Optional[str]] = mapped_column(String(256))
    password: Mapped[str] = mapped_column(String(1024))
    role: Mapped[str] = mapped_column(String(256))
    unsafekey: Mapped[Optional[str]] = mapped_column(String(1024))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r}, password={self.password!r}, role={self.role!r}, unsafekey={self.unsafekey!r})"

"""

user -> id, email, name, password, role, fiscal barcode (optional)
item:        get, patch, put, delete
user:        get, patch, put, delete
roles:       get, patch, put, delete
transaction: get, patch, put, delete
"""