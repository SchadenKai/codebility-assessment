from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.engine import get_session


router = APIRouter(prefix="/carts", tags=["carts"])


@router.post("")
def add_product_to_cart(db_session: Session = Depends(get_session)):
    pass


@router.get("")
def get_all_items_for_user(db_session: Session = Depends(get_session)):
    pass


@router.patch("/{product_id}")
def update_item_quantity(product_id: int, db_session: Session = Depends(get_session)):
    pass


@router.patch("/{product_id}")
def delete_item(product_id: int, db_session: Session = Depends(get_session)):
    pass
