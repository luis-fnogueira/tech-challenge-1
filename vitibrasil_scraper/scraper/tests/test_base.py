import unittest
from vitibrasil_scraper.scraper.base import BaseScraper

class TestBaseScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = BaseScraper()

    def test_parse_number(self):
        """Test the number parsing functionality with various inputs"""
        test_cases = [
            ("1.234", 1234),
            ("-", None),
            ("", None),
            ("abc", None),
            ("1.234.567", 1234567),
            ("123", 123)
        ]

        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                result = self.scraper._parse_number(input_text)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 