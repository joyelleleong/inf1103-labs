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

# global inventory
inventory = Inventory()

def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)

                for product_id, product_data in data.items():
                    product_type = product_data["type"]
                    if product_type == "physical":
                        product = PhysicalProduct(
                            product_id,
                            product_data["name"],
                            float(product_data["price"]),
                            int(product_data["stock"]),
                            float(product_data["weight"])
                        )
                    elif product_type == "digital":
                        product = DigitalProduct(
                            product_id,
                            product_data["name"],
                            float(product_data["price"]),
                            int(product_data["stock"]),
                            float(product_data["download_size"])
                        )
                    else:
                        print(f"Unknown product type for product ID {product_id}.")
                        continue
                    inventory.products[product_id] = product

            print("Inventory loaded successfully.")

        except (json.JSONDecodeError, KeyError, ValueError, TypeError):
            print("Error loading inventory file.")
    else:
        print("inventory.json not found. Starting with an empty inventory.")


def save_inventory():
    data = {}

    for product_id, product in inventory.get_all_products().items():
        data[product_id()] = product.to_dict()

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")

def add_product():
    print("\nAdd Product")

    product_id = input("Enter product ID: ")

    if inventory.search_product(product_id) is not None:
        print("Product ID already exists. Please use a unique ID.")
        return

    product_name = input("Enter product name: ")

    try:
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

        print("Select product type:")
        print("1. Physical Product")
        print("2. Digital Product")

        product_type = input("Enter choice (1 or 2): ")

        if product_type == "1":
            weight = float(input("Enter product weight (in kg): "))
            if weight < 0:
                print("Weight cannot be negative.")
                return
            product = PhysicalProduct(product_id, product_name, price, stock, weight)

        elif product_type == "2":
            download_size = float(input("Enter product download size (in MB): "))
            if download_size < 0:
                print("Download size cannot be negative.")
                return
            product = DigitalProduct(product_id, product_name, price, stock, download_size)

        else:
            print("Invalid product type selected.")
            return

        inventory.add_product(product)
    except ValueError:
        print("Invalid input. Please enter numeric values for price, stock, weight, and download size.")

def update_stock():
    print("\nUpdate Stock")
    product_id = input("Enter product ID: ")
    product = inventory.search_product(product_id)

    if product is not None:
        print("Product found.")
        print("Product Name:" , product.get_name())
        print("Current Stock:", product.get_stock())
        return

    try:
        new_stock = int(input("Enter new stock quantity: "))
        product.update_stock(new_stock)
    except ValueError:
        print("Please enter a valid number for stock.")

    else:
        print("Product not found in inventory.")

def search_product():
    print("\nSearch Product")
    product_id = input("Enter product ID: ")
    product = inventory.search_product(product_id)

    if product is not None:
        print("Product found.")
        product.display_information()
        print(product.get_fulfulment_info())

        if isinstance(product, CanBeShipped):
            print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
    else:
        print("Product not found in inventory.")

# main menu 
def main():

    load_inventory()

    while True:

        print("\nInventory Management System")
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Product Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product()

        elif choice == "3":
            update_stock()

        elif choice == "4":
            search_product()

        elif choice == "5":
            save_inventory()

        elif choice == "6":
            print("Saving inventory before exiting...")
            save_inventory()

            print(
                "Thank you for using the "
                "Inventory Management System."
            )
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
