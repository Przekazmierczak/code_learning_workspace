# TODO
import re

def main():
    text = input("Text: ")

    L = countLetters(text) / countWords(text) * 100
    S = countSentences(text) / countWords(text) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    roundedIndex = round(index)
    if (roundedIndex <= 1):
        print("Before Grade 1")
    elif (roundedIndex >= 16):
        print("Grade 16+")
    else:
        print(f"Grade {roundedIndex}")

def countLetters(text):
    regex = r"[A-Z]|[a-z]"
    letters = len(list(re.finditer(regex, text)))
    return letters

def countWords(text):
    regex = r"[A-Z]|[a-z]*[\w]"
    words = len(list(re.finditer(regex, text)))
    return words

def countSentences(text):
    regex = r"[A-Z][\w\s\d\,\'\;\:\"\(\)\[\]\%\$\&]*(\.)|[A-Z][\w\s\d\,\'\;\:\"\(\)\[\]\%\$\&]*(\?)|[A-Z][\w\s\d\,\'\;\:\"\(\)\[\]\%\$\&]*(\!)"
    sentences = len(list(re.finditer(regex, text)))
    return sentences

if __name__ == "__main__":
        main()