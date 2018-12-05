from flask import Flask
from app import routes

App = Flask(__name__)


from config import Config

App.config.from_object(Config)
