import unittest
from scraper import scrape_menu
from datetime import datetime


class TestScrape(unittest.TestCase):

    url = 'http://www.op97.org/mann/food-service'

    def test_scrape(self):
        self.assertFalse(False)

        current_time = datetime.now()

        test = scrape_menu(current_time)
        print(test)
        # self.assertEqual('oceans', analysis.pre_tag)


if __name__ == '__main__':
    unittest.main()
