from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'You Will Never Guess.'

from . import routes