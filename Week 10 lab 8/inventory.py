from canbeshipped import CanBeShipped

class Inventory:
    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        product_id = product.get_product_id()

        if product_id in self.__products:
            print("Product ID already exists. Please use a unique ID.")
        else:
            self.__products[product_id] = product

    def search_product(self, product_id):
        return self.__products.get(product_id, None)

    def display_all(self):
        print ("\nCurrent Inventory")
        print ("-" * 40)

        if len(self.__products) == 0:
            print("No products in inventory.")
            return

        for product in self.__products.values():
            product.display_information()
            print(product.get_fulfulment_info())

            if isinstance(product, CanBeShipped):
                print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
                print("-" * 40)

    def get_all_products(self):
        return self.__products