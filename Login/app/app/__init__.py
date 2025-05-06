from flask import Flask

def app_web():

    app = Flask(__name__)
    app.config['SECRET_KEY']="clave muy secreta"

    from .routes import main
    app. register_blueprint(main)

    return app