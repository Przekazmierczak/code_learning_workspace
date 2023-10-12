import csv
import sys

def main():
    if len(sys.argv) != 3:
        sys.exit("Command expects exactly two command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Files need to be csv's files")
    else:
        try:
            file = open(sys.argv[2], "r")
            file.close()
        except FileNotFoundError:
            try:
                changed_list = change_list(sys.argv[1])
            except FileNotFoundError:
                sys.exit("File not found")
            save_file(changed_list, sys.argv[2])
        else:
            sys.exit("File already exist")

def change_list(file_location):

    new_list = []
    with open(file_location, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            # Change first line
            if row[0] == "name":
                row.append(row[1])
                row[0] = "first"
                row[1] = "last"
            # Change other lines
            else:
                last, first = row[0].split(", ")
                row.append(row[1])
                row[0] = f"{first}"
                row[1] = f"{last}"
            new_list.append(row)
    return new_list

def save_file(changed_list, new_file_location):
    with open(new_file_location, "a") as file:
        for list_element in changed_list:
            row = ""
            # Separate elements with ","
            for element in list_element:
                row += element +","
            # Format string (remove last comma + add new line)
            row = row.rstrip()[:-1] + "\n"
            file.write(row)

if __name__ == "__main__":
    main()