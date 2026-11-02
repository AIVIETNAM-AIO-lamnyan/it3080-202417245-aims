import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchByTitleTests(unittest.TestCase):
    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King"),
            DigitalVideoDisc("Star Wars"),
        ]

    def test_search_is_case_insensitive(self):
        self.assertEqual(search_by_title(self.dvds, "lion"), [self.dvds[0]])

    def test_search_returns_empty_list_when_unmatched(self):
        self.assertEqual(search_by_title(self.dvds, "aladdin"), [])


if __name__ == "__main__":
    unittest.main()
