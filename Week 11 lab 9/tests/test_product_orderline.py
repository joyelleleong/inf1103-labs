import unittest

from supplier import Supplier
from product_factory import ProductFactory
from order_line import OrderLine


class TestValidation(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001",
            "ABC Supplier",
            "abc@gmail.com"
        )

    def create_product(self):
        return ProductFactory.create(
            "physical", "P001", "Desk Lamp",
            25.00, 10, self.supplier, weight=1.0
        )

    def test_zero_price(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P001", "Desk Lamp",
                0, 10, self.supplier, weight=1.0
            )

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P001", "Desk Lamp",
                -10, 10, self.supplier, weight=1.0
            )

    def test_negative_stock(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P001", "Desk Lamp",
                25.00, -1, self.supplier, weight=1.0
            )

    def test_zero_order_quantity(self):
        product = self.create_product()

        with self.assertRaises(ValueError):
            OrderLine(product, 0)

    def test_negative_order_quantity(self):
        product = self.create_product()

        with self.assertRaises(ValueError):
            OrderLine(product, -1)


if __name__ == "__main__":
    unittest.main()