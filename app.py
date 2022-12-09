# import libraries
import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp

# Create application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///laptop.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results")
def results():
    brand = request.args.get("q")

    #Price:
    string_budget = request.args.get("p")
    budget = string_budget.split(",")
    min_range_price = int(budget[0])
    max_range_price = int(budget[1])

    #Weight:
    string_weight = request.args.get("k")
    weight = string_weight.split(",")
    min_range_weight = weight[0]
    max_range_weight = weight[1]

    #Screensize:
    string_screensize = request.args.get("e")
    screensize = string_screensize.split(",")
    min_range_size = screensize[0]
    max_range_size = screensize[1]


    #Gaming:
    if request.args.get("g") == "Gaming":
        gaming_laptops = db.execute("SELECT * FROM laptops WHERE Category = 'Gaming'")
    else:
        gaming_laptops = db.execute("SELECT * FROM laptops")

    #touchscreen:
    if request.args.get("o") == "Touchscreen":
        touchscreen_laptops = db.execute("SELECT * FROM laptops WHERE Screen LIKE '%Touchscreen%'")
    else:
        touchscreen_laptops = db.execute("SELECT * FROM laptops")

    results = db.execute("SELECT * FROM laptops WHERE Manufacturer = ? AND Price BETWEEN ? AND ? AND Weight BETWEEN ? AND ? AND Screensize BETWEEN ? AND ?", brand, min_range_price, max_range_price, min_range_weight, max_range_weight, min_range_size, max_range_size)

    final_results = []
    for i in range(len(results)):
        for j in range(len(gaming_laptops)):
            for k in range(len(touchscreen_laptops)):
                if results[i] == gaming_laptops[j] == touchscreen_laptops[k]:
                    final_results.append(results[i])

    #Only want to display two options:
    if len(final_results) < 2:
        return jsonify(final_results)


    end_results = []
    for i in range(2):
       end_results.append(final_results[i])

    return jsonify(end_results) 