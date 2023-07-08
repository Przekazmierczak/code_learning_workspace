    if request.method == "POST":
        sell_shares = int(request.form.get("shares"))
        sell_symbol = request.form.get("symbol")
        sell_price = lookup(sell_symbol)['price']
        sell_actual_shares = db.execute("SELECT shares FROM stock WHERE user_id = ? and symbol = ?;", session["user_id"], sell_symbol)[0]['shares']
        if sell_shares > sell_actual_shares:
            comment = "Not enough shares!"
            return render_template("sell.html", tables=tables, current_cash=current_cash, grand_total=grand_total, comment=comment)
        sell_actual_shares = sell_actual_shares - sell_shares
        print(sell_actual_shares)
        db.execute("UPDATE stock SET shares = ? WHERE user_id = ? AND symbol = ?;",sell_actual_shares, session["user_id"], sell_symbol)
        test = db.execute("SELECT shares FROM stock WHERE user_id = ? AND symbol = ?;", session["user_id"], sell_symbol)
        print(test)
        current_cash = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])[0]['cash']
        current_cash = current_cash + sell_price * sell_shares
        db.execute("UPDATE users SET cash = ? WHERE id = ?",current_cash, session["user_id"])

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
        grand_total = usd(grand_total)

        return render_template("sell.html", tables=tables, current_cash=current_cash, grand_total=grand_total)

    else:
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
        grand_total = usd(grand_total)
        return render_template("sell.html", tables=tables, current_cash=current_cash, grand_total=grand_total)