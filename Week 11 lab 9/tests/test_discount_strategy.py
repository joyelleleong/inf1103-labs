import unittest

from supplier import Supplier
from product_factory import ProductFactory
from order_line import OrderLine
from order import Order

from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount


class TestDiscountStrategy(unittest.TestCase):

    def setUp(self):
        supplier = Supplier(
            "S001",
            "ABC Supplier",
            "abc@gmail.com"
        )

        product = ProductFactory.create(
            "physical", "P001", "Test Product",
            25.00, 20, supplier, weight=1.0
        )

        self.order = Order("O001")
        self.order.add_order_line(product, 10)

    def test_no_discount(self):
        self.assertEqual(NoDiscount().apply(250), 250)

    def test_percentage_discount(self):
        self.assertEqual(
            PercentageDiscount(10).apply(250), 225
        )

    def test_bulk_discount(self):
        self.assertEqual(
            BulkDiscount(200, 20).apply(250), 230
        )

    def test_student_discount(self):
        self.assertEqual(
            StudentDiscount().apply(250), 237.5
        )

    def test_change_discount_strategy(self):
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(self.order.calculate_total(), 230)

        self.order.set_discount(PercentageDiscount(10))
        self.assertEqual(self.order.calculate_total(), 225)

    def test_order_without_discount(self):
        self.assertEqual(self.order.calculate_total(), 250)


if __name__ == "__main__":
    unittest.main()