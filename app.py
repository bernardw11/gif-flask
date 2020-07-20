# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)

GIPHY_KEY = "xiiHwNzg3ajxC7yUqqsIB2HZWvUGpNpq"

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/yourgif', methods = ["GET", "POST"])
def yourgif():
    if request.method == "POST":
        choice = request.form['gifchoice']
        image = getImageUrlFrom(choice, GIPHY_KEY)
        return render_template("yourgif.html", time = datetime.now(), image = image)
    else:
        return "bruh error."