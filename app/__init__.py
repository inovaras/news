from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.Config')


db = SQLAlchemy(app)

from . import models

app_context = app.app_context()
app_context.push()

from . import views