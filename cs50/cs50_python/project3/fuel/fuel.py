while True:
    fraction = input("Fraction: ")

    try:
        [x, y] = fraction.split("/")
    except ValueError:
        print("Input need to be in x/y format")
    else:
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print("First and second value need to be an integer")
        else:
            if x > y:
                print("First value can not be bigger than second")
            else:
                try:
                    percentage = round(x/y * 100)
                except ZeroDivisionError:
                    print("Second value can not be 0")
                else:
                    if percentage >= 99:
                        print("F")
                    elif percentage <= 1:
                        print("E")
                    else:
                        print(f"{percentage}%")
                    break
