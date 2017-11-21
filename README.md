# Career Day - Software Engineering

This repository contains information on how to program a computer, including a sample program that serves the [Smines City Technology website](https://smines.city). This was developed for my daughter's kindergarten classroom.

## How To Program A Computer - Presentation

A [brief slideshow presentation](https://docs.google.com/presentation/d/1b_1pT_NTi1K51UKJafgZk6ReqeyPi49H2iAuveSjHaE/edit?usp=sharing) for the kids.


## Learning to Program / Resources
 * [Best Apps and Websites for Learning Programming](https://www.commonsense.org/education/top-picks/best-apps-and-websites-for-learning-programming-and-coding)

 * [Code Play Learn](https://www.codeplaylearn.com) is a local independent coding school for kids with a branch in Oak Park. Classes are typically offered for kids in grades 1-12.

 * [Crash Course on Computer
   Science](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo)
   and [Crash Course for Kids: The Engineering
   Process](https://www.youtube.com/playlist?list=PLhz12vamHOnZ4ZDC0dS6C9HRN5Qrm0jHO)

 * [Learn more about Margaret Hamilton](https://en.wikipedia.org/wiki/Margaret_Hamilton_(scientist))

 * [Introduction to Simple Web Applications (like this one) with Flask](http://www.compjour.org/lessons/flask-single-page/)

## How does this work?
A small python app scrapes information from the school lunch calendar and displays it, along with data from a weather API. It is [deployed to heroku](https://devcenter.heroku.com/articles/getting-started-with-python) and built using a [lightweight python web framework called Flask](http://flask.pocoo.org). It also uses:
 * [Paper CSS Framework](https://www.getpapercss.com) for style / design of the html markup.
 * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for scraping data from the calendar page.
 * [Dark Sky API package](https://github.com/ZeevG/python-forecast.io) and [Skycons](https://blog.darksky.net/skycons-unobtrustive-animated-weather-icons/).
   * Set your own API key using `heroku config:set DARKSKY_API_KEY=<yours>`

### Local Development
You can start a local flask server with this command:
`FLASK_APP=app.py FLASK_DEBUG=1 DARKSKY_API_KEY=<your_key> flask run

### Tests
Tests can be run using the `nosetests` command.

### Pseudocode
Parsing the calendar on the school lunch table is a good example of a common
programming task. Less of an academic exercise and more of a puzzle, it
provides a good example of how to use pseudocode to arrive at a solution.

#### Function 1. Find the next relevant menu day
Use this logic (in order) to determine what day's menu we want to display.
This assumes that the school calendar always displays all weekdays in the month.
You can find this pseudocode implemented in the [date_to_display function](./util.py#L4).
```
 * Make a call to the date / time library to find out what day it is.
 * If it is between 11am on Friday and 11am on Monday, we are likely interestedin Monday's menu.
 * If it is before 11am on a weekday, we are likely interested in the current day's menu.
 * If it is after 11am on a weekday, we are likely interested in the next day's menu.
 * Return the chosen day (for use in the function below).
```

#### Function 2. Look up the menu item corresponding with a menu day
Once we know the day of the month we are interested in, we need to
pull the menu for that day from the calendar. The calendar is [represented as an html table element](./tests/calendarcontent.html#L738). This means the [table is composed](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics) of rows `<tr>` and data `<td>` elements. You can find this pseudocode implemented in the [menu_for_day function](./scraper.py#L6).

On a side note, [Web APIs](https://www.programmableweb.com/news/what-api-exactly/analysis/2015/12/03) are popular because they often provide this type of data without the need to scrape pages, etc. For example, this application uses a [weather API](https://darksky.net/dev) to display the day's weather.
```
 * Search for a <td> with data equal to the day we are interested in.
   * If it is not found, search for the next highest day.
 * Store the position of the found <td> element, where 1-5 correspond to M-F.
 * Access the next <tr> and pull the data from the <td> in the position stored above.
 * Return the day's menu data to the user interface for display.
```
