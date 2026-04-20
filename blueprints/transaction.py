from flask import Blueprint
from typing import List
from sqlalchemy import DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from blueprints.item import Item
from blueprints.user import User
from models import Base, db
from decimal import *

transactions = Blueprint('transactions', __name__, url_prefix="/transactions")

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    datetime: Mapped[DateTime] = mapped_column(DateTime())
    paid: Mapped[bool] = mapped_column(Boolean())

    operators: Mapped[List["User"]] = relationship()
    items: Mapped[List["Item"]] = relationship()

    def __repr__(self) -> str:
        return f"Transaction(id={self.id!r}, datetime={self.datetime!r}, paid={self.paid!r})"

"""
item:        get, post, patch, delete
user:        get, post, patch, delete
transaction: get, post, patch, delete
roles:       get, post, patch, delete
"""