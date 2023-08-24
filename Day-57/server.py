from flask import Flask, render_template
from random import randint
import datetime as dt
import requests
import json


app = Flask(__name__)

@app.route("/")
def home_page():
    random_number = randint(0, 9)
    return render_template("index.html", num=random_number, date=dt.datetime.now().year)

@app.route("/<name>")
def user(name):
    parameters = {"name": name}
    response = requests.get("https://api.genderize.io", params=parameters)
    gender = response.json()["gender"]
    response = requests.get("https://api.agify.io", params=parameters)
    age = response.json()["age"]
    return render_template("user.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)