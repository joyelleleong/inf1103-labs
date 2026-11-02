import json
import os
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from canbeshipped import CanBeShipped
from inventory import Inventory

# physical product class - add weight
# digital product class - add download_size

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
                    inventory.add_product(product)

            print("Inventory loaded successfully.")

        except (json.JSONDecodeError, KeyError, ValueError, TypeError):
            print("Error loading inventory file.")
    else:
        print("inventory.json not found. Starting with an empty inventory.")


def save_inventory():
    data = {}

    for product_id, product in inventory.get_all_products().items():
        data[product_id] = product.to_dict()

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
