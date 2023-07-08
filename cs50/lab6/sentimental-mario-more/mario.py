# TODO

def main():

    while True:
        size = input("What is the size: ")
        if size.isnumeric():
            size = int(size)
            if size > 0 and size < 9:
                break
    counter = 1
    for i in range(size):
        left(size, counter)
        print("  ", end = "")
        right(counter)
        print("")
        counter += 1

def left(size, counter):

    for i in range(size):
        if i < (size - counter):
            print(" ", end = "")
        else:
            print("#", end = "")

def right(counter):

    for i in range(counter):
        print("#", end = "")

if __name__ == "__main__":
        main()