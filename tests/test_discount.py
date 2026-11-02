import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartDiscountTests(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.items.append(DigitalVideoDisc("Test DVD", cost=100))

    def test_applies_discount_to_total(self):
        self.assertEqual(self.cart.total_cost_with_discount(20), 80)

    def test_rejects_discount_over_100_percent(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)

    def test_rejects_negative_discount(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(-1)


if __name__ == "__main__":
    unittest.main()
