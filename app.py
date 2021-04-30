import os
import logging

from flask import Flask, render_template, request, jsonify

template_dir = os.path.abspath('./template')
static_dir = os.path.abspath('./static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = os.environ["FLASK_KEY"]

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.INFO)


@app.route('/')
def init_app():
    app.logger.info(app.secret_key)
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
