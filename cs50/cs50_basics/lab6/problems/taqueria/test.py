import re

text = input('Text: ')

regex = r"[A-Z][\w\s\d\,\'\;\:\"\(\)\[\]\%\$\&]*(\.)|[A-Z][\w\s\d\,\'\;\:\"\(\)\[\]\%\$\&]*(\?)|[A-Z][\w\s\d\,\'\;\:\"\(\)\[\]\%\$\&]*(\!)"

list2 = list(re.finditer(regex, text))
sentences = len(list(re.finditer(regex, text)))

print(list2)
print(sentences)