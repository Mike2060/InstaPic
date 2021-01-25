from flask import Flask, render_template, request, redirect, url_for, session
from flask import Flask
import os

def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    UPLOAD_FOLDER = 'static/img/UserImage'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    # a simple page that says hello
    from . import InstaPic
    app.register_blueprint(InstaPic.bp)
    app.url_map.strict_slashes = False
    return app
