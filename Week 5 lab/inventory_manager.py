# add_product()
# update_stock()
# search_product()
# display_all()

# load_inventory()
# save_inventory()

# display add update search save and exit 
import json
import os 

# current inventory data
inventory = {
    "P001": {
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    "P002": {
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    "P003": {
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
}

#load inventory from file
def load_inveontry():
    global inventory
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            inventory = json.load(file)
            print("Inventory loaded successfully.")
    else:
        print("No existing inventory found.")
        print("Starting with an empty inventory.")
        inventory = {}

#save inventory to file
def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
        print("Inventory saved successfully to inventory.json.")

# display all products in the inventory
def display_all():
    print("\nCurrent Inventory:")
    print("-" * 60)

    if len(inventory) == 0:
        print("No products in the inventory.")
        return

    for product_id, product in inventory.items():
        print(
            f"ID: {product_id} |"
            f"Name: {product['name']} |"
            f"Price: ${product['price']:.2f} |"
            f"Stock: {product['stock']} |" 
        )
    print("-" * 60)

# add a new product to the inventory
def add_product():
    print ("\nAdd New Product")

    product_id = input("Enter Product ID: ")
    if product_id in inventory:
        print("Product already exists.")
        return

    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    inventory[product_id] = {
        "name": product_name,
        "price": price,
        "stock": stock
    }

    print("Product added successfully.")

# update stock of an existing product
def update_stock():
    print("\nUpdate Stock")

    product_id = input("Enter Product ID:")

    if product_id in inventory:
        print("Product found.")
        print("Name:", inventory[product_id]["name"])
        print("Current Stock:", inventory[product_id]["stock"])
        new_stock = int(input("Enter new stock quantity: "))
        inventory[product_id]["stock"] = new_stock
        print("Stock updated successfully.")
    else:
        print("Product not found.")

#search product
def search_product():
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        product = inventory[product_id]
        print("Product found:")
        print("ID:", product_id)
        print("Name:", product["name"])
        print(f"Price: ${product['price']:.2f}")
        print("Stock:", product["stock"])
    else:
        print("Product not found.")