from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from product import Product

def test_relationships() -> None:

    print("\n========== LAB 8 TESTS ==========")

    # Create supplier
    supplier = Supplier(
        "S100",
        "ABC Electronics",
        "abc@gmail.com"
    )

    # Create products
    laptop = PhysicalProduct(
        "P100", "Laptop", 1500.0, 10, 2.5, supplier
    )

    template = DigitalProduct(
        "P101", "Canva Template", 20.0, 50, 10.0, supplier
    )

    # --------------------------------
    # 1. ASSOCIATION
    # --------------------------------

    print("\n1. ASSOCIATION")

    laptop.get_supplier().display_information()

    # --------------------------------
    # 2. AGGREGATION
    # --------------------------------

    print("\n2. AGGREGATION")

    inventory_a = Inventory()
    inventory_b = Inventory()

    inventory_a.add_product(laptop)

    print("Removing laptop from Inventory A.")

    inventory_a.remove_product("P100")

    print("Adding laptop to Inventory B.")

    inventory_b.add_product(laptop)

    print("Laptop still exists:", laptop.get_name())

    # --------------------------------
    # 3. COMPOSITION
    # --------------------------------

    print("\n3. COMPOSITION")

    order1 = Order("O001")

    order1.add_order_line(laptop, 2)
    order1.add_order_line(template, 3)

    order1.display_order()

    # Same Product, different OrderLine
    order2 = Order("O002")

    order2.add_order_line(laptop, 1)

    print(
        "Are the two OrderLine objects the same?",
        order1.order_lines[0] is order2.order_lines[0]
    )

    # --------------------------------
    # 4. POLYMORPHISM AND LSP
    # --------------------------------

    print("\n4. POLYMORPHISM AND LSP")

    products = [laptop, template]

    for product in products:

        product.display_information()

        print(product.get_fulfulment_info())

        print("Current stock:", product.get_stock())

        # Both subclasses can use Product's method
        product.update_stock(20)

    print("\n========== TESTS COMPLETED ==========")

if __name__ == "__main__":
    test_relationships()