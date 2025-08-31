from sqlalchemy.orm import Session
from app.models.order import Order

def create_order(db: Session, description: str, user_id: int):
    new_order = Order(description=description, user_id=user_id)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def get_orders_by_user(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).all()
 
