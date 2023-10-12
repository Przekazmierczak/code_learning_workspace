amount_due = 50
while True:
    print(f"Amount Due: {amount_due}")
    while True:
        insert = int(input("Insert Coin: "))
        if insert == 25 or insert == 10 or insert == 5:
            break
        else:
            print(f"Amount Due: {amount_due}")
    amount_due -= insert
    if amount_due <= 0:
        change_owned = amount_due * -1
        print(f"Change Owned: {change_owned}")
        break