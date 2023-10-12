text = input("camelCase: ")
snake = ""
for letter in text:
    if letter.isupper():
        snake = snake + "_" + letter.lower()
    else:
        snake = snake + letter

print(f"snake_case: {snake}")