def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        if percentage != None:
            string = gauge(percentage)
            break
    print(string)

def convert(fraction):
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
                    return percentage

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()