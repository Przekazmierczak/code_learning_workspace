def main():

    word = input("Input: ")
    word = shorten(word)
    print(f"Output: {word}")

def shorten(word):

    changed_text = ""
    for letter in word:
        if letter not in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U",):
            changed_text += letter
    return changed_text

if __name__ == "__main__":
    main()
