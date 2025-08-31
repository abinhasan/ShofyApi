from sqlalchemy.orm import Session
from app.crud import order as crud_order
from app.models.order import Order

def create_order_for_user(db: Session, description: str, user_id: int) -> Order:
    return crud_order.create_order(db, description, user_id)

def get_user_orders(db: Session, user_id: int):
    return crud_order.get_orders_by_user(db, user_id)
 
