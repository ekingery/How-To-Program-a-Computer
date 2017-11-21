import unittest
import os
from scraper import scrape_menu, date_to_display
from datetime import datetime
import pytz


class TestScrape(unittest.TestCase):

    url = 'http://www.op97.org/mann/food-service'

    def test_datecalc(self):
        current_dt = datetime.now().astimezone(tz=pytz.timezone('US/Central'))
        self.assertGreaterEqual(date_to_display(current_dt), 1)
        self.assertLessEqual(date_to_display(current_dt), 31)

        am_date = datetime.strptime(
            'Monday, November 20, 2017 - 7:05 AM', '%A, %B %d, %Y - %I:%M %p'
        )
        pm_date = datetime.strptime(
            'Monday, November 20, 2017 - 12:38 PM', '%A, %B %d, %Y - %I:%M %p'
        )
        self.assertEqual(date_to_display(am_date), 20)
        self.assertEqual(date_to_display(pm_date), 21)

    def test_scrape(self):
        self.assertFalse(False)

        current_path = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        test_file = os.path.join(current_path, 'calendarcontent.html')
        with open(test_file, 'r') as opened_file:
            testcontent = opened_file.read()

        fixed_date = datetime.strptime(
            'Tuesday, November 14, 2017 - 8:10 AM', '%A, %B %d, %Y - %I:%M %p'
        )
        test = scrape_menu(fixed_date, testcontent)
        self.assertIn('Tortilla', str(test))
        self.assertNotIn('Spaghetti', str(test))


if __name__ == '__main__':
    unittest.main()
