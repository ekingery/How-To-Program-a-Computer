# Comments start with # and are used to explain the code
# to other programmers and often to your future self
# They are ignored by the programming language

# load module for dealing with logging
import logging

# load the flask web framework
from flask import Flask

# define the application as a flask object
app = Flask(__name__)

# setup the logger to stream logs to stdout
stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('smines_city app startup')

# Import the routes that serve web pages
import smines_city.views  # noqa is a message to the flake8 syntax checker

# Run the application when you run `python app.py`
if __name__ == '__main__':
    app.run()
