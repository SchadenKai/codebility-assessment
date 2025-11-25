from fastapi import APIRouter


router = APIRouter(prefix="/products", tags=["products"])


@router.post("")
def create_product_api():
    pass


@router.get("")
def list_producuts_api():
    pass


@router.get("/{id}")
def get_product_api(id: int):
    pass


@router.patch("/{id}")
def update_product_api(id: int):
    pass


@router.delete("/{id}")
def delete_product_api(id: int):
    pass
