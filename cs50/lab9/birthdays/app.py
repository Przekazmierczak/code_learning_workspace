import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        day = request.form.get("day")
        month = request.form.get("month")

        if not name.isalpha():
            note = "Invalid Name"
        elif not day.isnumeric() or not month.isnumeric():
            note = "Day/Month need to be numeric"
        elif int(day) < 1 or int(day) > 31:
            note = "Invalid Day"
        elif int(month) < 1 or int(month) > 12:
            note = "Invalid Month"
        else:
            note = ""
            db.execute("INSERT INTO birthdays (name, day, month) VALUES (?, ?, ?);", name, day, month)

        birthdays = db.execute("SELECT * FROM birthdays;")
        return render_template("index.html", birthdays=birthdays, note=note)

    else:

        # TODO: Display the entries in the database on index.html\
        birthdays = db.execute("SELECT * FROM birthdays;")
        return render_template("index.html", birthdays=birthdays)

@app.route("/remove", methods=["GET", "POST"])
def remove():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM birthdays WHERE id = ?", id)
    birthdays = db.execute("SELECT * FROM birthdays;")
    return render_template("index.html", birthdays=birthdays)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_id = request.form.get("id")
    birthdays = db.execute("SELECT * FROM birthdays;")
    edit_id = int(edit_id)
    return render_template("index.html", birthdays=birthdays, edit_id=edit_id)

@app.route("/change", methods=["GET", "POST"])
def change():
    # Add conditions for input like name isalpha etc.
    changed_name = request.form.get("changed_name")
    changed_day = request.form.get("changed_day")
    changed_month = request.form.get("changed_month")
    changed_id = request.form.get("changed_id")
    if changed_name:
        db.execute("UPDATE birthdays SET name = ? WHERE id = ?;", changed_name, changed_id)
    if changed_day:
        db.execute("UPDATE birthdays SET day = ? WHERE id = ?;", changed_day, changed_id)
    if changed_month:
        db.execute("UPDATE birthdays SET month = ? WHERE id = ?;", changed_month, changed_id)

    birthdays = db.execute("SELECT * FROM birthdays;")
    return render_template("index.html", birthdays=birthdays)

