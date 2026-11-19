from discount_strategy import DiscountStrategy

class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total