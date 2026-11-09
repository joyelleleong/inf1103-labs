from product import Product


class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        if self.find_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
        else:
            self.products.append(product)
            print("Product added successfully.")

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)

        if product is not None:
            self.products.remove(product)
            print("Product removed successfully.")
        else:
            print("Product not found.")

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("-" * 40)

        if len(self.products) == 0:
            print("No products in inventory.")
            return

        for product in self.products:
            product.display_information()
            print(product.get_fulfulment_info())

    def get_all_products(self) -> list[Product]:
        return self.products