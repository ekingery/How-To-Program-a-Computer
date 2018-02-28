# load a couple of flask functions for templates and file serving
from flask import request, redirect, render_template, send_from_directory
# load modules for dealing with dates and times
from datetime import datetime
import pytz  # timezones

# import the app so we can register routes to serve
from smines_city import app
# load our own functions from the smines_city module
from smines_city.util import date_to_display
from smines_city.scraper import scrape_menu
from smines_city.weather import get_weather


# Serve a web page at the root of the URL
@app.route('/')
def homepage():
    # This is the main function that serves the web page

    # redirect ssl requests to http (heroku does not support SSL on free dynos)
    if request.url.startswith('https://'):
        url = request.url.replace('https://', 'http://', 1)
        redirect(url, 301)

    local_tz = pytz.timezone('US/Central')
    current_dt = local_tz.localize(datetime.now())
    display_date = date_to_display(current_dt)
    formatted_date = display_date.strftime("%A, %B %d")

    # check the weather first
    forecast = get_weather(display_date)
    if forecast is None:
        return render_template('notready.html')

    current = forecast.currently()
    hourly = forecast.hourly()
    daily = forecast.daily()
    nextday = daily.data[0]
    temp = {
        'now': int(current.temperature),
        'high': int(nextday.d['temperatureMax']),
        'low': int(nextday.d['temperatureMin'])
    }
    summary = 'Currently ' + current.summary + '. ' + \
        hourly.summary + ' ' + daily.summary

    # get the menu for today
    items = scrape_menu(current_dt)

    # Return the html markup we use to serve the page
    return render_template(
        'index.html', date=formatted_date, menu_items=items, temp=temp,
        weather_icon=current.icon, weather_summary=summary,
        current_summary=current.summary
    )


# Serve images locally
@app.route('/images/<path:path>')
def serve_images(path):
    return send_from_directory('static/images', path)


# Serve favicon
@app.route('/favicon.ico')
def serve_favicon():
    return send_from_directory('static/images', 'favicon.png')


# Serve css locally
@app.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('static/css', path)


# Serve js locally
@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('static/js', path)
