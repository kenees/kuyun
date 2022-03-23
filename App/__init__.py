from flask import Flask
from App.middleware import load_middleware
from App.settings import envs
from App.api import init_view

def create_app(env):
    app = Flask(__name__, static_folder='../webapp', static_url_path='/')
    app.config.from_object(envs.get(env))
    init_view(app)
    load_middleware(app)
    return app

