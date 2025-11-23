import reflex as rx
from typing import TypedDict
from app.states.cart_state import CartState


class WishlistItem(TypedDict):
    id: int
    name: str
    price: int
    image: str
    category: str
    rating: int


class WishlistState(rx.State):
    items: list[WishlistItem] = [
        {
            "id": 1,
            "name": "Premium Fried Groundnuts",
            "price": 250,
            "image": "/premium_fried_groundnuts.png",
            "category": "Fried",
            "rating": 5,
        },
        {
            "id": 3,
            "name": "Pure Natural Honey (500g)",
            "price": 800,
            "image": "/honey_pure_natural.png",
            "category": "Honey",
            "rating": 5,
        },
    ]

    @rx.event
    def remove_from_wishlist(self, item_id: int):
        self.items = [i for i in self.items if i["id"] != item_id]

    @rx.event
    async def move_to_cart(self, item: dict):
        cart_state = await self.get_state(CartState)
        cart_state.add_to_cart(item, 1)
        self.remove_from_wishlist(item["id"])