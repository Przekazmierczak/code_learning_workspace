from tabulate import tabulate
import csv
import sys

headers = []
table = []
if len(sys.argv) != 2:
    print("Command line must have one argument")
elif not sys.argv[1].endswith(".csv"):
    print("Command line argument need to be csv file")
else:
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)

            first_time = True
            for row in reader:
                if first_time == True:
                    headers.extend(row)
                else:
                    table.append(row)
                first_time = False
    except FileNotFoundError:
        print("File not found")

print(tabulate(table, headers, tablefmt="grid"))