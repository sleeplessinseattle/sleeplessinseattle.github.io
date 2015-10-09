# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.scss import Scss
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_pyfile('settings.py')
Scss(app, static_dir='static/css', asset_dir='static/css/src')
freezer = Freezer(app)