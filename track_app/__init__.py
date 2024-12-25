from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from track_app.routes import main

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///track.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
