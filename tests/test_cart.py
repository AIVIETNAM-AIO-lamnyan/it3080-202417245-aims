import contextlib
import io
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

    def test_add_dvd_to_non_full_cart(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test DVD")

        with contextlib.redirect_stdout(io.StringIO()):
            added = cart.add_dvd(dvd)

        self.assertTrue(added)
        self.assertEqual(cart.items, [dvd])

    def test_remove_dvd_from_cart(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test DVD")
        cart.items.append(dvd)

        with contextlib.redirect_stdout(io.StringIO()):
            removed = cart.remove_dvd(dvd)

        self.assertTrue(removed)
        self.assertEqual(cart.items, [])

    def test_total_cost(self):
        cart = Cart()
        cart.items.extend([
            DigitalVideoDisc("First DVD", cost=10.0),
            DigitalVideoDisc("Second DVD", cost=15.5),
        ])

        self.assertEqual(cart.total_cost(), 25.5)


if __name__ == "__main__":
    unittest.main()
