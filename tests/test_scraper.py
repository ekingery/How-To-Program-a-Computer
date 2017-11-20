import unittest
import os
from scraper import scrape_menu
from datetime import datetime


class TestScrape(unittest.TestCase):

    url = 'http://www.op97.org/mann/food-service'

    def test_scrape(self):
        self.assertFalse(False)

        current_time = datetime.now()

        current_path = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        test_file = os.path.join(current_path, 'calendarcontent.html')
        with open(test_file, 'r') as opened_file:
            testcontent = opened_file.read()

        test = scrape_menu(current_time, testcontent)
        self.assertIn('Spaghetti', str(test))


if __name__ == '__main__':
    unittest.main()
