from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Lightweight Track Builder!"

# Register blueprint in __init__.py
