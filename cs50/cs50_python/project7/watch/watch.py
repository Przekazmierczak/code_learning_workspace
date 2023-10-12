import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    link = get_link(s)
    matches = re.search(r"^https?://(?:www.)?youtube.com/embed/(.+)$", link)
    if matches:
        match = matches.group(1)
        match = f"https://youtu.be/{match}"
        return match
    else:
        return None


def get_link(link):
    splited = link.split(" ")
    for element in splited:
        if element.startswith("src="):
            src = element
    src = src.replace("src=", "")
    src = src.split('"')
    # Correct link always in the middle (between "")
    return src[1]


if __name__ == "__main__":
    main()