from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):
    def __init__(self, product_id: int, name: str,
                 price: float, stock: int,
                 supplier: Supplier):

        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.supplier: Supplier = supplier

    def get_product_id(self) -> int:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.supplier

    def update_stock(self, new_stock: int) -> None:
        if new_stock < 0:
            print("Stock cannot be negative.")
        else:
            self.__stock = new_stock
            print("Stock updated successfully.")

    def display_information(self) -> None:
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

        print("\nSupplier Information:")
        self.supplier.display_information()

    @abstractmethod
    def get_fulfulment_info(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass