from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Lightweight Track Builder!"

# Don't forget to register the blueprint in __init__.py
