from flask import render_template
from taskmanager import app, db, models
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")