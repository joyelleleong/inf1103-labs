import json
import os

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from inventory import Inventory
from order import Order
from canbeshipped import CanBeShipped


# Global inventory
inventory = Inventory()


# ==========================================
# LOAD INVENTORY
# ==========================================

def load_inventory() -> None:

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)

                for product_id, product_data in data.items():

                    # Load supplier information
                    supplier_data = product_data.get(
                        "supplier",
                        {
                            "supplier_id": "S001",
                            "name": "Default Supplier",
                            "contact_email": "default@gmail.com"
                        }
                    )

                    supplier = Supplier(
                        supplier_data["supplier_id"],
                        supplier_data["name"],
                        supplier_data["contact_email"]
                    )

                    product_type = product_data["type"]

                    if product_type == "physical":

                        product = PhysicalProduct(
                            product_id,
                            product_data["name"],
                            float(product_data["price"]),
                            int(product_data["stock"]),
                            float(product_data["weight"]),
                            supplier
                        )

                    elif product_type == "digital":

                        product = DigitalProduct(
                            product_id,
                            product_data["name"],
                            float(product_data["price"]),
                            int(product_data["stock"]),
                            float(product_data["download_size"]),
                            supplier
                        )

                    else:
                        print(f"Unknown product type: {product_id}")
                        continue

                    inventory.add_product(product)

            print("Inventory loaded successfully.")

        except (json.JSONDecodeError, KeyError, ValueError, TypeError):
            print("Error loading inventory file.")

    else:
        print("inventory.json not found. Starting empty inventory.")


# ==========================================
# SAVE INVENTORY
# ==========================================

def save_inventory() -> None:

    data = {}

    for product in inventory.get_all_products():

        product_id = product.get_product_id()
        data[product_id] = product.to_dict()

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")


# ==========================================
# ADD PRODUCT
# ==========================================

def add_product() -> None:

    print("\nAdd Product")

    product_id = input("Enter product ID: ")

    if inventory.find_product(product_id) is not None:
        print("Product ID already exists.")
        return

    product_name = input("Enter product name: ")

    try:
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

        # Create Supplier object independently
        print("\nEnter Supplier Information")

        supplier_id = input("Enter supplier ID: ")
        supplier_name = input("Enter supplier name: ")
        supplier_email = input("Enter supplier email: ")

        supplier = Supplier(
            supplier_id,
            supplier_name,
            supplier_email
        )

        print("\nSelect product type:")
        print("1. Physical Product")
        print("2. Digital Product")

        product_type = input("Enter choice: ")

        if product_type == "1":

            weight = float(input("Enter product weight (kg): "))

            if weight < 0:
                print("Weight cannot be negative.")
                return

            product = PhysicalProduct(
                product_id,
                product_name,
                price,
                stock,
                weight,
                supplier
            )

        elif product_type == "2":

            download_size = float(
                input("Enter download size (MB): ")
            )

            if download_size < 0:
                print("Download size cannot be negative.")
                return

            product = DigitalProduct(
                product_id,
                product_name,
                price,
                stock,
                download_size,
                supplier
            )

        else:
            print("Invalid product type.")
            return

        inventory.add_product(product)

    except ValueError:
        print("Invalid numeric input.")


# ==========================================
# UPDATE STOCK
# ==========================================

def update_stock() -> None:

    print("\nUpdate Stock")

    product_id = input("Enter product ID: ")

    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product found.")
    print("Product Name:", product.get_name())
    print("Current Stock:", product.get_stock())

    try:
        new_stock = int(input("Enter new stock quantity: "))
        product.update_stock(new_stock)

    except ValueError:
        print("Please enter a valid number.")


# ==========================================
# SEARCH PRODUCT
# ==========================================

def search_product() -> None:

    print("\nSearch Product")

    product_id = input("Enter product ID: ")

    product = inventory.find_product(product_id)

    if product is not None:

        print("Product found.")

        product.display_information()

        print(product.get_fulfulment_info())

        if isinstance(product, CanBeShipped):
            print(
                f"Shipping Cost: "
                f"${product.calculate_shipping_cost():.2f}"
            )

    else:
        print("Product not found in inventory.")


# ==========================================
# TEST LAB 8 RELATIONSHIPS
# ==========================================

def test_relationships() -> None:

    print("\n========== LAB 8 TESTS ==========")

    # Create supplier
    supplier = Supplier(
        "S100",
        "ABC Electronics",
        "abc@gmail.com"
    )

    # Create products
    laptop = PhysicalProduct(
        "P100", "Laptop", 1500.0, 10, 2.5, supplier
    )

    template = DigitalProduct(
        "P101", "Canva Template", 20.0, 50, 10.0, supplier
    )

    # --------------------------------
    # 1. ASSOCIATION
    # --------------------------------

    print("\n1. ASSOCIATION")

    laptop.get_supplier().display_information()

    # --------------------------------
    # 2. AGGREGATION
    # --------------------------------

    print("\n2. AGGREGATION")

    inventory_a = Inventory()
    inventory_b = Inventory()

    inventory_a.add_product(laptop)

    print("Removing laptop from Inventory A.")

    inventory_a.remove_product("P100")

    print("Adding laptop to Inventory B.")

    inventory_b.add_product(laptop)

    print("Laptop still exists:", laptop.get_name())

    # --------------------------------
    # 3. COMPOSITION
    # --------------------------------

    print("\n3. COMPOSITION")

    order1 = Order("O001")

    order1.add_order_line(laptop, 2)
    order1.add_order_line(template, 3)

    order1.display_order()

    # Same Product, different OrderLine
    order2 = Order("O002")

    order2.add_order_line(laptop, 1)

    print(
        "Are the two OrderLine objects the same?",
        order1.order_lines[0] is order2.order_lines[0]
    )

    # --------------------------------
    # 4. POLYMORPHISM AND LSP
    # --------------------------------

    print("\n4. POLYMORPHISM AND LSP")

    products = [laptop, template]

    for product in products:

        product.display_information()

        print(product.get_fulfulment_info())

        print("Current stock:", product.get_stock())

        # Both subclasses can use Product's method
        product.update_stock(20)

    print("\n========== TESTS COMPLETED ==========")


# ==========================================
# MAIN MENU
# ==========================================

def main() -> None:

    load_inventory()

    while True:

        print("\nInventory Management System")
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Product Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("7. Run Lab 8 Relationship Tests")

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

            print("Thank you for using the Inventory Management System.")
            print("Exiting the program.")
            break

        elif choice == "7":
            test_relationships()

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()