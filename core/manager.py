# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_cors import CORS
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
CORS(app)
started_date = datetime.now()

# config database
app_settings = os.getenv(
    'APP_SETTINGS',
    'config.DevelopmentConfig'
)
app.config.from_object(app_settings)
db = SQLAlchemy(app)
db.init_app(app)
marsh = Marshmallow(app)

# model
from models import user

# blueprint
from controllers.status import bp_status
app.register_blueprint(bp_status)
