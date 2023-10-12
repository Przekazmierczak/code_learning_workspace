import validators

def main():
    valid = validation(input("Email: "))
    print(valid)

def validation(email):
    valid = validators.email(email)
    if valid == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
     main()