import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""
    tables = db.execute("SELECT symbol, shares FROM stock WHERE user_id = ?", session["user_id"])
    grand_total = 0
    for table in tables:
        price = lookup(table['symbol'])['price']
        price_usd= usd(price)
        table['price'] = price_usd
        total = table['shares'] * price
        grand_total = grand_total + total
        total = usd(total)
        table['total'] = total
    current = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])[0]['cash']
    grand_total = grand_total + current
    grand_total = usd(grand_total)

    if request.method == "POST":
        buy_shares = request.form.get("shares")
        # To avoid error
        if buy_shares == "":
            buy_shares = 0
        buy_shares = int(buy_shares)
        buy_symbol = request.form.get("symbol")
        buy_price = lookup(buy_symbol)['price']
        buy_actual_shares = db.execute("SELECT shares FROM stock WHERE user_id = ? and symbol = ?;", session["user_id"], buy_symbol)[0]['shares']
        if buy_shares <= 0 or buy_shares == None:
            comment = "Number of shares need to positive."
            current = usd(current)
            return render_template("index.html", tables=tables, current=current, grand_total=grand_total, comment=comment)
        if buy_shares * buy_price > current:
            comment = "You do not have enough money."
            current = usd(current)
            return render_template("index.html", tables=tables, current=current, grand_total=grand_total, comment=comment)
        buy_new_shares = buy_actual_shares + buy_shares
        db.execute("UPDATE stock SET shares = ? WHERE user_id = ? AND symbol = ?;",buy_new_shares, session["user_id"], buy_symbol)
        current = current - buy_price * buy_shares
        db.execute("UPDATE users SET cash = ? WHERE id = ?",current, session["user_id"])
        for table in tables:
            if table['symbol'] == buy_symbol:
                table['shares'] = buy_new_shares
        # Update history
        db.execute("INSERT INTO history (user_id, symbol, date, price, shares) VALUES (?, ?, ?, ?, ?);", session["user_id"], buy_symbol, date.today(), buy_price, buy_shares)
        current = usd(current)
        return render_template("index.html", tables=tables, current=current, grand_total=grand_total)

    else:
        current = usd(current)
        return render_template("index.html", tables=tables, current=current, grand_total=grand_total)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        buy_symbol = request.form.get("symbol").upper()
        buy_shares = request.form.get("shares")
        # To avoid error
        if buy_shares == "":
            buy_shares = 0
        stock_price = lookup(buy_symbol)
        if stock_price == None:
            comment = "Symbol does not exist"
            return render_template("buy.html", comment=comment)
        stock_price = stock_price['price']
        user_id = session["user_id"]
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?;", user_id)[0]['cash']
        # check if shares not 0 or smaller than 0
        if int(buy_shares) <= 0:
            comment = "Number of shares need to positive."
            return render_template("buy.html", comment=comment)
        # check if user has enought money
        if (int(buy_shares) * stock_price) > user_cash:
            comment = "You do not have enough money."
            return render_template("buy.html", comment=comment)
        check = db.execute("SELECT * FROM stock WHERE symbol = ? AND user_id = ?", buy_symbol, user_id)
        if len(check) == 0:
            db.execute("INSERT INTO stock (user_id, symbol, shares) VALUES (?, ?, ?);", user_id, buy_symbol, buy_shares)
        if len(check) == 1:
            actual_shares = db.execute("SELECT shares FROM stock WHERE user_id = ? AND symbol = ?;", user_id, buy_symbol)[0]['shares']
            new_shares = actual_shares + int(buy_shares)
            db.execute("UPDATE stock SET shares = ? WHERE user_id = ? AND symbol = ?;", new_shares, user_id, buy_symbol)
        # Update history
        db.execute("INSERT INTO history (user_id, symbol, date, price, shares) VALUES (?, ?, ?, ?, ?);", user_id, buy_symbol, date.today(), stock_price, buy_shares)
        new_cash = user_cash - (int(buy_shares) * stock_price)
        db.execute("UPDATE users SET cash = ? WHERE id = ?;",new_cash ,user_id)
        comment = "Shares added to your wallet."
        return render_template("buy.html", comment=comment)
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    tables = db.execute("SELECT date, id, symbol, price, shares  FROM history WHERE user_id = ?;", session["user_id"])
    for table in tables:
        balance = - (table['price'] * table['shares'])
        if balance >= 0:
            table['balance_sell'] = usd(balance)
        else:
            table['balance_buy'] = usd(balance)
        table['balance'] = balance
        table['price'] = usd(table['price'])
    tables.reverse()
    return render_template("history.html", tables=tables)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            comment = "Wrong symbol format"
            return render_template("quote.html", comment=comment)
        stock = lookup(symbol)
        if stock == None:
            comment = "Symbol does not exist"
            return render_template("quote.html", comment=comment)
        price = usd(stock['price'])
        return render_template("quoted.html", stock=stock, price=price)
    else:
        return render_template("quote.html")

@app.route("/quoted", methods=["GET", "POST"])
@login_required
def quoted():
    """Back button"""
    if request.method == "POST":
        return render_template("quote.html")
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        new_username = request.form.get("username")
        new_password = request.form.get("password")
        confirm_new_password = request.form.get("confirm_password")
        check_rows = db.execute("SELECT * FROM users WHERE username = ?", new_username)
        if len(check_rows) == 1:
            comment = "username already exist"
            return render_template("register.html", comment=comment)
        if not new_password == confirm_new_password:
            comment = "passwords do not match"
            return render_template("register.html", comment=comment)
        hashed_password = generate_password_hash(new_password)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?);", new_username, hashed_password)
        return render_template("login.html")
    else:

        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    tables = db.execute("SELECT symbol, shares FROM stock WHERE user_id = ?", session["user_id"])
    grand_total = 0
    for table in tables:
        price = lookup(table['symbol'])['price']
        price_usd= usd(price)
        table['price'] = price_usd
        total = table['shares'] * price
        grand_total = grand_total + total
        total = usd(total)
        table['total'] = total
    current_cash = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])[0]['cash']
    grand_total = grand_total + current_cash
    grand_total = usd(grand_total)

    if request.method == "POST":
        sell_shares = request.form.get("shares")
        # To avoid error
        if sell_shares == "":
            sell_shares = 0
        sell_shares = int(sell_shares)
        sell_symbol = request.form.get("symbol")
        sell_price = lookup(sell_symbol)['price']
        sell_actual_shares = db.execute("SELECT shares FROM stock WHERE user_id = ? and symbol = ?;", session["user_id"], sell_symbol)[0]['shares']
        if sell_shares <= 0:
            comment = "Number of shares need to positive."
            current_cash = usd(current_cash)
            return render_template("sell.html", tables=tables, current_cash=current_cash, grand_total=grand_total, comment=comment)
        if sell_shares > sell_actual_shares:
            comment = "Not enough shares!"
            current_cash = usd(current_cash)
            return render_template("sell.html", tables=tables, current_cash=current_cash, grand_total=grand_total, comment=comment)
        sell_new_shares = sell_actual_shares - sell_shares
        db.execute("UPDATE stock SET shares = ? WHERE user_id = ? AND symbol = ?;",sell_new_shares, session["user_id"], sell_symbol)
        current_cash = current_cash + sell_price * sell_shares
        db.execute("UPDATE users SET cash = ? WHERE id = ?",current_cash, session["user_id"])
        for table in tables:
            if table['symbol'] == sell_symbol:
                table['shares'] = sell_new_shares
        # Remove from table if shares reach 0
        if sell_new_shares == 0:
            db.execute("DELETE FROM stock WHERE shares = 0;")
            for table in tables:
                if table['symbol'] == sell_symbol:
                    tables.remove(table)
        # Update history
        db.execute("INSERT INTO history (user_id, symbol, date, price, shares) VALUES (?, ?, ?, ?, ?);", session["user_id"], sell_symbol, date.today(), sell_price, -(sell_shares))
        current_cash = usd(current_cash)
        return render_template("sell.html", tables=tables, current_cash=current_cash, grand_total=grand_total)
    else:
        current_cash = usd(current_cash)
        return render_template("sell.html", tables=tables, current_cash=current_cash, grand_total=grand_total)
