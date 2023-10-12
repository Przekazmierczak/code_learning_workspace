menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

value = 0
while True:
    try:
        item = input("Item: ").title()
    # brak after user click ctr + d
    except EOFError:
        print("")
        break
    else:
        if item in menu:
            value += menu[item]
            formated_value = format(value,".2f")
            print(f"Total: {formated_value}$")