def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    i = 0
    numeric = False
    for letter in s:
        # Check if vanity plate start with at least two letters
        if (i == 0 or i == 1) and not letter.isalpha():
            return False
        # Check if vanity plate contain a maximum of 6 characters
        if i > 5:
            return False
        if not letter.isalpha() and not letter.isnumeric():
            return False
        # Check if numbers are not in the middle of a plate
        if letter.isnumeric() and numeric == False:
            numeric = True
            # Check if the first number used is ‘0’
            if letter == "0":
                return False
        # Check if word do not contain periods, spaces, or punctuation marks
        if letter.isalpha() and numeric == True:
            return False
        i += 1
    # Check if vanity plate contain a minimum of 2 characters
    if i > 2:
        return True
    else:
        return False

if __name__ == "__main__":
    main()