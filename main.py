# pip install flask
from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="BomYi")

@app.route("/hello")
def hello():
    return 'Hello!'

app.run("0.0.0.0")
