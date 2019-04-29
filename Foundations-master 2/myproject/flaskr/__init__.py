import os

from flask import Flask

# create_app is the application factory function


def create_app(test_config=None):
    # creates, configures the app and creates the Flask instance.
    #__name__ = current Python module
    app = Flask(__name__, instance_relative_config=True)
    # sets some default configuration that the app will use
    app.config.from_mapping(
        SECRET_KEY='dev',
        # path where the SQLite database file will be saved
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
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
    #app function?
    
    # Importing and registering the blueprints
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    #just return once
    return app