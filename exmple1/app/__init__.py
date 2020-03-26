from flask import Flask
from app.apis  import init_api
from app.extend import init_extend
from app.middleware import load_middleware
from app.settings import envs



def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get("develop"))
    init_extend(app)
    init_api(app=app)
    load_middleware(app)
    return app
