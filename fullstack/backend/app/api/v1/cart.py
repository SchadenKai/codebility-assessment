from fastapi import APIRouter


router = APIRouter(prefix="/carts", tags=["carts"])


@router.post("")
def add_product_to_cart():
    pass


@router.get("")
def get_all_items_for_user():
    pass


@router.patch("/{product_id}")
def update_item_quantity(product_id: int):
    pass


@router.patch("/{product_id}")
def delete_item(product_id: int):
    pass
