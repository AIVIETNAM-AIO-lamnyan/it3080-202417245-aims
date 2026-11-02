import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation"),
        ]

    def test_search_by_category_returns_matching_dvds(self):
        self.assertEqual(
            search_by_category(self.dvds, "Animation"),
            [self.dvds[0], self.dvds[2]],
        )

    def test_search_by_category_returns_empty_list_when_unmatched(self):
        self.assertEqual(search_by_category(self.dvds, "Comedy"), [])

    def test_search_by_title_remains_available(self):
        self.assertEqual(search_by_title(self.dvds, "The"), [self.dvds[0]])


if __name__ == "__main__":
    unittest.main()
