def main():
    array = []
    get_array(array)
    print_array(array)
    
    answers = []
    with open("words.txt", "r") as file:
        for word in file:
            word = word.rstrip('\n')
            if len(word) > 3:
                checked_word = check_word(word, array)
                if checked_word != None:
                    answers.append(checked_word)

    # sorted_answers = sorted(answers, key=lambda tup: tup[0])
    for answer in answers:
        print(answer)

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
            z = [0]
            if letter == word_array[0]:
                # create locations[i] lists
                for i in range(20):
                    globals()[f'locations{i}'] = []
                # create records[i] lists - track already used letters
                for i in range(20):
                    globals()[f'records{i}'] = []
                globals()[f'locations{z[-1]}'] = [[x, y]]
                # row and column are numbers showing locations of letters around checked letter
                while True:
                    if len(globals()[f'locations{z[-1]}']) > 0:
                        for row in range(3):
                                for column in range(3):
                                    # skip the middle location
                                    middle_condition = True
                                    if row == 1 and column == 1:
                                        middle_condition = False
                                    if (globals()[f'locations{z[-1]}'][0][0] + (row - 1)) >= 0 and (globals()[f'locations{z[-1]}'][0][0] + (row - 1)) < 5 and (globals()[f'locations{z[-1]}'][0][1] + (column - 1)) >= 0 and (globals()[f'locations{z[-1]}'][0][1] + (column - 1)) < 5:
                                        if word_array[z[-1]+1] == array[globals()[f'locations{z[-1]}'][0][0] + (row - 1)][globals()[f'locations{z[-1]}'][0][1] + (column - 1)] and middle_condition == True:
                                            # prevent from using previous numbers
                                            previous_condition = True
                                            for i in range(len(z) - 1):
                                                if globals()[f'locations{z[-1]}'][0][0] + (row - 1) == globals()[f'records{i}'][0][0] and globals()[f'locations{z[-1]}'][0][1] + (column - 1) == globals()[f'records{i}'][0][1]:
                                                    previous_condition = False
                                            if previous_condition == True:
                                                globals()[f'location{z[-1] + 1}'] = []
                                                globals()[f'location{z[-1] + 1}'].append(globals()[f'locations{z[-1]}'][0][0] + (row - 1))
                                                globals()[f'location{z[-1] + 1}'].append(globals()[f'locations{z[-1]}'][0][1] + (column - 1))
                                                globals()[f'locations{z[-1] + 1}'].append(globals()[f'location{z[-1] + 1}'])
                    if len(globals()[f'locations{z[-1]}']) > 0:
                        record = globals()[f'locations{z[-1]}'].copy()
                        globals()[f'records{z[-1]}'].insert(0, record[0])
                        globals()[f'locations{z[-1]}'].pop(0)
                    if len(globals()[f'locations{z[-1] + 1}']) > 0:
                        z.append(z[-1] + 1)
                    if len(globals()[f'locations{z[-1]}']) == 0:
                        z.pop()
                    if len(z) == 0:
                        break
                    if len(z) == len(word_array):                      
                        record = globals()[f'locations{z[-1]}'].copy()
                        globals()[f'records{z[-1]}'].extend(record)
                        records = []
                        for i in range(len(word_array)):
                            records.append(globals()[f'records{i}'][0])
                        return word, records
            y += 1
        x += 1

if __name__ == "__main__":
    main()