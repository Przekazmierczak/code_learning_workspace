expresion = input("Expresion: ")

[x, y, z] = expresion.split(" ")

x = int(x)
z = int(z)

if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*":
    answer = x * z
elif y == "/":
    answer = x / z

print(float(answer))