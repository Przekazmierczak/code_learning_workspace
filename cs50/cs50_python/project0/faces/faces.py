def main():
    # Get users input
    text = input()
    text = convert(text)
    # Print output
    print(text)

def convert(text):
    # Change emoticons into emoji
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()