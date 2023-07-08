# TODO
import math

def main():

    while True:
        change = input("Change owed: ")
        if isfloat(change) is True:
             change = float(change)
             if change > 0:
                break

    change = round(change, 2)

    coins = math.floor(change / 0.25)
    remain = round(change % 0.25, 2)

    coins += math.floor(remain / 0.10)
    remain = round(remain % 0.10, 2)

    coins += math.floor(remain / 0.05)
    remain = round(remain % 0.05, 2)

    coins += math.floor(remain / 0.01)

    print(coins)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
        main()