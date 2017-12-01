import requests
import bs4
from util import date_to_display


def menu_for_day(menu_table, day):
    rows = menu_table.find_all('tr')
    found_day = None
    # Loop for all rows in the table
    for row in rows:
        # Store the index of the position we are interested in
        i = 1
        # Loop for all data elements in each row
        for td in row.find_all('td'):
            # If we found the day we are looking for
            if (found_day):
                j = 1
                # loop for the data elements in the next row
                for td in row.find_all('td'):
                    # when the index matches, we have found the right menu data
                    if found_day == j:
                        # return the menu data from the td tag as a list
                        return td.contents
                    # increment the counter to the menu item
                    j += 1
            # Wrap the attempt to read the day in error handling
            try:
                # Cast the html values to a string and then to an int
                # This will error out when we don't find an integer,
                # but it's the easiest way to test if we have one
                dayval = int(str(td.contents[0]))
            except (ValueError, IndexError) as e:
                # Catch the errors because they aren't actually a problem,
                # We just don't have a value we care about, so move on
                dayval = 0
            # If we have a match between the data and the day we want
            if day == dayval:
                # store it, so we can pull the menu data from the next <tr>
                found_day = i
                # Break out of the inner loop, now that we have a winner
                break
            # increment the counter to the next day
            i += 1

    # If we don't return from the loops above, we did not find the menu
    return "Menu not found"


def format_items(menu):
    menu_items = []
    for item in menu:
        if type(item) is bs4.element.NavigableString:
            # cast to a string and strip spacing
            menu_items.append(str(item).strip())
        elif type(item) is bs4.element.Tag:
            if len(item.contents) > 0:
                for content in item.contents:
                    if type(content) is bs4.element.NavigableString:
                        # cast contents to a string and strip spacing
                        menu_items.append(str(content.strip()))

    # remove empty strings
    menu_items = list(filter(None, menu_items))
    return menu_items


def scrape_menu(current_datetime, scraped_content=None):
    search_day = date_to_display(current_datetime).day
    menu_url = 'http://www.op97.org/mann/food-service'
    if not scraped_content:
        try:
            req = requests.get(menu_url)
        except requests.exceptions.RequestException as e:
            msg = 'Exception: ' + str(e) + 'scraping: ' + menu_url
            print(msg)
        scraped_content = req.text

    soup = bs4.BeautifulSoup(scraped_content, 'html.parser')
    calendar_table = soup.find('table', class_='table-striped')
    menu = menu_for_day(calendar_table, search_day)
    items = format_items(menu)
    return items
