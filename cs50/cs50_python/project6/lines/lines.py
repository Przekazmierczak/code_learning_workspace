import sys

if len(sys.argv) != 2:
    sys.exit("Command line should have one argument")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Argmument need to be a python file")
else:
    i = 0
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File not found")
    else:
        for line in lines:
            if not line.strip().startswith("#") and line.strip() != "":
                i += 1
    print(i)