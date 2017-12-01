# Comments start with # and are used to explain the code
# to other programmers and often to your future self
# They are ignored by the programming language

# load the flask web framework
from flask import Flask
# package that redirects non ssl (http) requests to ssl (https)
from flask_sslify import SSLify

# define the application as a flask object
app = Flask(__name__)
sslify = SSLify(app)  # redirect the non-secure (http) version to https

# Import the routes that serve web pages
import smines_city.views  # noqa is a message to the flake8 syntax checker

# Run the application when you run `python app.py`
if __name__ == '__main__':
    app.run()
