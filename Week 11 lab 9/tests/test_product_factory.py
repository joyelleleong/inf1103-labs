import unittest

from supplier import Supplier
from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


class TestProductFactory(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001",
            "ABC Supplier",
            "abc@gmail.com"
        )

    def test_create_physical_product(self):
        product = ProductFactory.create(
            "physical", "P001", "Desk Lamp",
            25.00, 10, self.supplier, weight=1.0
        )

        self.assertIsInstance(product, PhysicalProduct)
        self.assertEqual(product.get_product_id(), "P001")
        self.assertEqual(product.get_name(), "Desk Lamp")

    def test_create_digital_product(self):
        product = ProductFactory.create(
            "digital", "D001", "Photo Editor",
            49.90, 100, self.supplier, download_size=1.0
        )

        self.assertIsInstance(product, DigitalProduct)
        self.assertEqual(product.get_product_id(), "D001")

    def test_unknown_product_type(self):
        with self.assertRaisesRegex(ValueError, "Unknown product type"):
            ProductFactory.create(
                "service", "S001", "Installation",
                30.00, 5, self.supplier
            )


if __name__ == "__main__":
    unittest.main()