from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(self, product_id: int, name: str,
                 price: float, stock: int,
                 download_size: float, supplier: Supplier):

        super().__init__(
            product_id, name, price, stock, supplier
        )

        self.__download_size = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")
        print("-" * 40)

    def get_fulfulment_info(self) -> str:
        return "This product is delivered digitally."

    def to_dict(self) -> dict:
        return {
            "type": "digital",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "download_size": self.__download_size,
            "supplier": {
                "supplier_id": self.supplier.get_supplier_id(),
                "name": self.supplier.get_name(),
                "contact_email": self.supplier.get_contact_email()
            }
        }