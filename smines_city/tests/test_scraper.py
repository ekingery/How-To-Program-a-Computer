import unittest
import os
import pytz
from datetime import datetime
from smines_city.scraper import scrape_menu
from smines_city.util import date_to_display


class TestScrape(unittest.TestCase):

    url = 'http://www.op97.org/mann/food-service'

    def test_datecalc(self):
        # test today
        local_tz = pytz.timezone('US/Central')
        current_dt = local_tz.localize(datetime.now())
        self.assertGreaterEqual(date_to_display(current_dt).day, 1)
        self.assertLessEqual(date_to_display(current_dt).day, 31)

        # test the morning and afternoon transition for a couple of dates
        am_date = datetime.strptime(
            'Monday, November 20, 2017 - 7:05 AM', '%A, %B %d, %Y - %I:%M %p'
        )
        pm_date = datetime.strptime(
            'Monday, November 20, 2017 - 12:38 PM', '%A, %B %d, %Y - %I:%M %p'
        )
        thur_date = datetime.strptime(
            'Thursday, November 23, 2017 - 2:38 PM', '%A, %B %d, %Y - %I:%M %p'
        )
        self.assertEqual(date_to_display(am_date).day, 20)
        self.assertEqual(date_to_display(pm_date).day, 21)
        self.assertEqual(date_to_display(thur_date).day, 24)

        # test the weekend transition
        fri_date = datetime.strptime(
            'Friday, November 24, 2017 - 12:38 PM', '%A, %B %d, %Y - %I:%M %p'
        )
        sat_date = datetime.strptime(
            'Saturday, November 25, 2017 - 2:38 PM', '%A, %B %d, %Y - %I:%M %p'
        )
        self.assertEqual(date_to_display(fri_date).day, 27)
        self.assertEqual(date_to_display(sat_date).day, 27)

        # test a shift to the next month
        next_month_date = datetime.strptime(
            'Thursday, November 30, 2017 - 2:38 PM', '%A, %B %d, %Y - %I:%M %p'
        )
        self.assertEqual(date_to_display(next_month_date).day, 1)

    def test_scrape(self):
        self.assertFalse(False)

        current_path = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        test_file = os.path.join(current_path, 'calendarcontent.html')
        with open(test_file, 'r') as opened_file:
            testcontent = opened_file.read()

        self.assertIn('Tortilla', testcontent)
        self.assertIn('Spaghetti', testcontent)

        fixed_date = datetime.strptime(
            'Tuesday, November 14, 2017 - 8:10 AM', '%A, %B %d, %Y - %I:%M %p'
        )
        test = scrape_menu(fixed_date, testcontent)
        self.assertIn('Tortilla', str(test))
        self.assertNotIn('Spaghetti', str(test))


if __name__ == '__main__':
    unittest.main()
