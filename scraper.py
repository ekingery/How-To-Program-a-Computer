import requests
import bs4
from datetime import timedelta


def date_to_display(current_dt):
    MONDAY = 0
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
    day_index = current_dt.weekday()  # Monday = 0, Sunday = 6
    hour = current_dt.hour

    # Test for after 11am on Friday, all weekend, and Monday before 11am
    if day_index in [FRIDAY, SATURDAY, SUNDAY, MONDAY]:
        if FRIDAY == day_index and hour > 10:
            # Add three days to get Monday
            return current_dt + timedelta(3)
        if SATURDAY == day_index:
            # add two days to get Monday
            return current_dt + timedelta(2)
        if SUNDAY == day_index:
            # add one day to get Monday
            return current_dt + timedelta(1)
        if MONDAY == day_index and hour <= 10:
            return current_dt

    # At this point, we can simply test for before 11am
    if hour <= 10:
        # and return the current day if it's before 11am
        return current_dt

    # It is after 11am on a weekday, return the next day
    return current_dt + timedelta(1)


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
                # cast contents to a string and strip spacing
                menu_items.append(str(item.contents[0].strip()))

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
