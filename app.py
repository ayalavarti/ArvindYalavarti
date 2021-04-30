import os
import logging

from flask import Flask, render_template, request, jsonify
from google.cloud import datastore


template_dir = os.path.abspath('./templates')
static_dir = os.path.abspath('./public')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = os.environ["FLASK_KEY"]

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)


@app.route('/')
def init_app():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
