from product import Product
from canbeshipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def calculate_shipping_cost(self):
        return self.__weight * 5

    def get_fulfulment_info(self):
        return "This product requires physical shipping."

    def to_dict(self):
        data = {
            "type": "physical",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "weight": self.__weight
        }
        return data
