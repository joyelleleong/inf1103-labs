import json
import os 

# product class
# inventory class
# main menu
# add product
# display products
# update stock
# search product
# save and load json 
# exit

class Product:

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

    # Display product information
    def display_information(self):
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    # Convert object into dictionary for JSON
    def to_dict(self):
        return {
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        product_id = product.get_product_id()

        if product_id in self.products:
            print("Product ID already exists. Please use a unique ID.")
        else:
            self.products[product_id] = product
            print("Product added successfully.")

    def search_product(self, product_id):
        return self.products.get(product_id, None)

    def display_all(self):
        print("\nCurrent Inventory:")
        print("-" * 60)

        if len(self.products) == 0:
            print("No products in inventory.")
            return

        for product in self.products.values():
            product.display_information()

        print("-" * 60)

    def get_all_products(self):
        return self.products

# load inventory from JSON file 
inventory = Inventory()

def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)

                for product_id, product_data in data.items():
                    product = Product(
                        product_id,
                        product_data["name"],
                        float(product_data["price"]),
                        int(product_data["stock"])
                    )
                    inventory.products[product_id] = product
            print("Inventory loaded successfully.")
        except (json.JSONDecodeError, KeyError, ValueError, TypeError):
            print("Error loading inventory file.")
    else:
        print("inventory.json not found." \
        "Starting with an empty inventory.")

def save_inventory():
    data = {}

    for product_id, product in inventory.get_all_products().items():
        data[product_id] = product.to_dict()

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

# function to display the main menu
def display_all():
    inventory.display_all()


def add_product():
    print("\nAdd New Product")

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

        product = Product(product_id, product_name, price, stock)
        inventory.add_product(product)

    except ValueError:
        print("Please enter valid numbers for price and stock.")


def update_stock():
    print("\nUpdate Product Stock")

    product_id = input("Enter product ID: ")
    product = inventory.search_product(product_id)

    if product is not None:
        print("Product found.")
        print("Name:" , product.get_name())
        print("Current Stock:", product.get_stock())

        try:
            new_stock = int(input("Enter new stock quantity: "))

            if new_stock < 0:
                print("Stock cannot be negative.")
                return

            product.update_stock(new_stock)
        except ValueError:
            print("Please enter a valid number for stock.")

    else:
        print("Product not found.")

def search_product():
    print("\nSearch Product")

    product_id = input("Enter product ID: ")
    product = inventory.search_product(product_id)

    if product is not None:
        print("Product found.")
        product.display_information()
    else:
        print("Product not found.")

# main function to run the program
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
            display_all()
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
            print("Thank you for using the Inventory Management System.")
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()