import requests
from bs4 import BeautifulSoup


def scrape_menu(current_datetime, scraped_content=None):
    menu_url = 'http://www.op97.org/mann/food-service'
    if not scraped_content:
        try:
            req = requests.get(menu_url)
        except requests.exceptions.RequestException as e:
            msg = 'Exception: ' + str(e) + 'scraping: ' + menu_url
            print(msg)
        scraped_content = req.text

    soup = BeautifulSoup(scraped_content, 'html.parser')
    calendar_table = soup.find('table', class_='table-striped')
    return calendar_table
