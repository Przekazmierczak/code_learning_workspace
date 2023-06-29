def main():
    array = []
    get_array(array)
    print_array(array)
    answers = []
    with open("words.txt", "r") as file:
        for word in file:
            word = word.rstrip('\n')
            if len(word) > 3:
                answer = check_word(word, array)
                if answer != None:
                    answers.append(answer)
    answers.sort(key = len)
    print(answers)

def get_array(array):
    n = 1
    for i in range(5):
        row = input(f'Row nr {n}: ')
        n += 1

        row_array = []
        for letter in row:
            row_array.extend(letter)
        array.append(row_array)

def print_array(array):
    for row in range(5):
        print(array[row])

def check_word(word, array):
    word_array = []
    for letter in word:
        word_array.extend(letter)

# x - row's number
# y - column's number 
# z - word's letter number
    x = 0
    while x < 5:
        y = 0
        for letter in array[x]:
            z = 0
            if letter == word_array[z]:
                locations = [[x, y]]
                records = [[x, y]]
                while z < (len(word) - 1):
                    z += 1
                    for i in range(len(locations)):
                        # row and column are numbers showing locations of letters around checked letter
                        for row in range(3):
                            for column in range(3):
                                # condition preventing from going back to used letters
                                condition = True
                                for record in records:
                                    if locations[0][0] + (row - 1) == record[0] and locations[0][1] + (column - 1) == record[1]:
                                        condition = False
                                if (locations[0][0] + (row - 1)) >= 0 and (locations[0][0] + (row - 1)) < 5 and (locations[0][1] + (column - 1)) >= 0 and (locations[0][1] + (column - 1)) < 5:
                                    if word_array[z] == array[locations[0][0] + (row - 1)][locations[0][1] + (column - 1)] and condition == True:
                                        location = []
                                        location.append(locations[0][0] + (row - 1))
                                        location.append(locations[0][1] + (column - 1))
                                        locations.append(location)
                                        records.append(location)
                        locations.pop(0)
                    if z == (len(word) - 1) and len(locations) > 0:
                        return(word)
            y += 1
        x += 1

if __name__ == "__main__":
    main()