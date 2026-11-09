from product import Product
from canbeshipped import CanBeShipped
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: int, name: str,
                 price: float, stock: int,
                 weight: float, supplier: Supplier):

        super().__init__(
            product_id, name, price, stock, supplier
        )

        self.__weight = weight

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 5

    def get_fulfulment_info(self) -> str:
        return "This product requires physical shipping."

    def to_dict(self) -> dict:
        return {
            "type": "physical",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "weight": self.__weight,
            "supplier": {
                "supplier_id": self.supplier.get_supplier_id(),
                "name": self.supplier.get_name(),
                "contact_email": self.supplier.get_contact_email()
            }
        }