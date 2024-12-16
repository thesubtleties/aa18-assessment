from flask import Flask
from .config import Configuration
from .routes import register_blueprints
from .models import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Configuration)

db.init_app(app)
Migrate(app, db)

register_blueprints(app)
