import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartLimitTests(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test DVD")

        for _ in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(dvd))

        self.assertFalse(cart.add_dvd(dvd))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)


if __name__ == "__main__":
    unittest.main()
