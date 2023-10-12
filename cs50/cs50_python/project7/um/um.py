import re


def main():
    print(count(input("Text: ")))


def count(s):
    matches = len(re.findall(r"((?:\W|^)+um(?:\W|$)+)", s, re.IGNORECASE))
    return matches

if __name__ == "__main__":
    main()