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