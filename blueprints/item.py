from flask import Blueprint, request
from typing import Optional
from sqlalchemy import String, Numeric
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Mapped, mapped_column
from models import Base, db
from decimal import *

getcontext().prec = 3

item = Blueprint('item', __name__, url_prefix="/item")

class Item(Base):
    __tablename__ = "items"
    
    barcode: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(1024))
    price: Mapped[Optional[Decimal]] = mapped_column(Numeric(precision=15, scale=3))
    # discounts need to be dealt about here

    def __repr__(self) -> str:
        return f"Item(barcode={self.barcode!r}, name={self.name!r}, price={self.price!r})"

@item.route('/get/<int:barcode>')
def get(barcode: int):
    item = db.session.get(Item, barcode)

    if not item: return {"error": "Item not found"}, 404

    return {
        "barcode": item.barcode,
        "name": item.name,
        "price": item.price
    }

@item.route('/new/<int:barcode>', methods=['POST'])
def new(barcode: int):
    name: str = request.args.get("name")
    try:
        price: Decimal = Decimal(request.args.get("price"))
    except InvalidOperation:
        return {"error": "Price is not a number"}

    if name == None: return {"error": "Missing name"}, 400
    if price == None: return {"error": "Missing price"}, 400

    item = Item(
        barcode=barcode,
        name=name,
        price=price
    )
    
    db.session.add(item)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {"error": "Failed to commit; item already exists"}

    return {
        "barcode": item.barcode,
        "name": item.name,
        "price": item.price
    }

@item.route('/edit/<int:barcode>', methods=['PATCH'])
def edit(barcode: int):
    name: str | None = request.args.get("name")
    try:
        price: Decimal | None = Decimal(request.args.get("price"))
    except InvalidOperation:
        return {"error": "Price is not a number"}
    except TypeError:
        price = None
    
    item = db.session.get(Item, barcode)
    if name != None: item.name = name
    if price != None: item.price = price
    db.session.commit()

    return {
        "barcode": item.barcode,
        "name": item.name,
        "price": item.price,
        "status": "ok"
    }

@item.route('/delete/<int:barcode>', methods=['DELETE'])
def delete(barcode: int):
    item = db.session.get(Item, barcode)
    if not item: return {"error": "Item not found"}, 404
    db.session.delete(item)
    db.session.commit()

    return {"status": "ok"}

"""
item:        get, patch, post, delete
user:        get, patch, post, delete
transaction: get, patch, post, delete
roles:       get, patch, post, delete
discount:    get, patch, post, delete

discount: quantity, type ($ or %), items (DEAL WITH LATER)

clients we need them

item -> name, code, price (optional)
"""