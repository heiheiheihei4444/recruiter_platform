from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()
migrate=Migrate()
cache=Cache(config={
    "CACHE_TYPE":"simple"
})

def init_extend(app):
    db.init_app(app)
    migrate.init_app(app,db)
    DebugToolbarExtension(app)
    cache.init_app(app)