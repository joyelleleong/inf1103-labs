import json
import os
from abc import ABC, abstractmethod

# physical product class - add weight
# digital product class - add download_size

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, new_stock):
        if new_stock < 0:
            print("Stock cannot be negative.")
        else:
            self.__stock = new_stock
            print("Stock updated successfully.")

    def display_information(self):
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    @abstractmethod
    def get_fulfulment_info(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

# physical product class
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

# digital product class
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfulment_info(self):
        return "This product is a delivered digitally."

    def to_dict(self):
        data = {
            "type": "digital",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "download_size": self.__download_size
        }
        return data

# inventory class
class Inventory:
    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        product_id = product.get_product_id()

        if product_id in self.__products:
            print("Product ID already exists. Please use a unique ID.")
        else:
            self.__products[product_id] = product
            print("Product added successfully.")

    def search_product(self, product_id):
        return self.__products.get(product_id, None)

    def display_all(self):
        print ("\nCurrent Inventory")
        print ("-" * 60)

        if len(self.__products) == 0:
            print("No products in inventory.")
            return

        for product in self.__products.values():
            product.display_information()
            print(product.get_fulfulment_info())

            if isinstance(product, CanBeShipped):
                print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")

        print("-" * 60) 

    def get_all_products(self):
        return self.__products.values()