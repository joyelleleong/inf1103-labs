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

