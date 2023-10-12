import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level >= 0:
            break

number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess >= 0:
            if number > guess:
                print("Too small!")
            elif number < guess:
                print("Too large!")
            else:
                print("Just right!")
                break