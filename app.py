# Comments start with # and are used to explain the code
# to yourself and other programmers!
# They are ignored by the programming language

# load a library for dealing with dates and times
from datetime import datetime

# load the flask web framework
from flask import Flask
# define the application as a flask object
app = Flask(__name__)


# Serve a web page at the root of the URL
@app.route('/')
def homepage():
    # This is our main function that serves the web page
    the_time = datetime.now().strftime("%A, %B %d, %Y at %l:%M %p")

    # This returns the html markup we use to serve the page
    return """
<h1>Smines City Technology Page</h1>
<p>Page loaded on {time}.</p>
    """.format(time=the_time)


# This is known as boilerplate code
# This particular boilerplate runs the application when you run `python app.py`
if __name__ == '__main__':
    app.run()
