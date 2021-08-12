import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env # noqa

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URI")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://")
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    


db = SQLAlchemy(app)

from taskmanager import routes # noqa