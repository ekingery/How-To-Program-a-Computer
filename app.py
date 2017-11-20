# Comments start with # and are used to explain the code
# to other programmers and often to your future self
# They are ignored by the programming language

# load modules for dealing with dates and times
from datetime import datetime
import pytz  # timezones

# load the flask web framework, along with the templating module for html
from flask import Flask, render_template
# define the application as a flask object
app = Flask(__name__)


# Serve a web page at the root of the URL
@app.route('/')
def homepage():
    # This is the main function that serves the web page
    current_time = datetime.now().astimezone(tz=pytz.timezone('US/Central'))
    formatted_time = current_time.strftime("%A, %B %d, %Y at %l:%M %p")

    # Return the html markup we use to serve the page
    return render_template('index.html', time=formatted_time)


# This is known as boilerplate code
# This particular boilerplate runs the application when you run `python app.py`
if __name__ == '__main__':
    app.run()
