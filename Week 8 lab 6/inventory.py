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