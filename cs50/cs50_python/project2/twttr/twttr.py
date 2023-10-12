text = input("Input: ")
changed_text = ""
for letter in text:
    if letter not in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U",):
        changed_text += letter
print(f"Output: {changed_text}")