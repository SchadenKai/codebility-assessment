from fastapi import APIRouter


router = APIRouter(prefix="/carts", tags=["carts"])

@router.get("/all")
def get_all_users_carts() -> list[any]:
    pass

@router.post("")
def add_product_to_cart() -> int:
    pass

@router.patch("")
def update_cart() -> int:
    pass

@router.delete("")
def delete_item_in_cart() -> int:
    pass