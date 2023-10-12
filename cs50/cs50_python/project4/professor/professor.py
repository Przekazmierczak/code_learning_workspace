import random


def main():
    points = 0
    level = get_level()
    for _ in range(10):
        first = generate_integer(level)
        second = generate_integer(level)
        correct_answer = first + second

        print(f"{first} + {second} = ", end="")
        try:
            user_answer = int(input())
        except ValueError:
            print("EEE")
        else:
            if correct_answer == user_answer:
                points += 1
            else:
                print("EEE")
    print(f"Score: {points}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= level <= 3:
                break
    return level


def generate_integer(level):
    random_int = random.randint(1 * pow(10, (level - 1)), pow(10, level))
    return random_int


if __name__ == "__main__":
    main()