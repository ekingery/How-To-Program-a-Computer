# Career Day - Software Engineering

This repository contains information on how to program a computer, including a sample program that serves the [Smines City Technology website](http://smines.city). This was developed for my daughter's kindergarten classroom.

## How To Program A Computer - Presentation

A [brief slideshow presentation](https://docs.google.com/presentation/d/1b_1pT_NTi1K51UKJafgZk6ReqeyPi49H2iAuveSjHaE/edit?usp=sharing) for the kids.


## Learning to Program / Resources
 * [Best Apps and Websites for Learning Programming](https://www.commonsense.org/education/top-picks/best-apps-and-websites-for-learning-programming-and-coding)

 * [Code Play Learn](https://www.codeplaylearn.com) is a local independent coding school for kids with a branch in Oak Park. Classes are typically offered for kids in grades 1-12.

 * [Introduction to Simple Web Applications with Flask](http://www.compjour.org/lessons/flask-single-page/)

 * [Learn more about Margaret Hamilton](https://en.wikipedia.org/wiki/Margaret_Hamilton_(scientist))

## How does this work?
A small python app scrapes information from the school lunch calendar and displays it, along with data from a weather API. It is [deployed to heroku](https://devcenter.heroku.com/articles/getting-started-with-python) and built using a [lightweight python web framework called Flask](http://flask.pocoo.org). It also uses:
 * [Paper CSS Framework](https://www.getpapercss.com) for style / design of the html markup.
 * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for scraping data from the calendar page.
 * [Dark Sky API package](https://github.com/ZeevG/python-forecast.io) and [Weather Icons](https://erikflowers.github.io/weather-icons/).

### Tests
Tests can be run using the `nosetests` command. 
