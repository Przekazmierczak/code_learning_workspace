import json
from flask import Flask, render_template, request
# from threading import Thread

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        array = []
        # array that helps give all input letters number from 1 to 25
        letters_array = []
        get_array(array, letters_array)
        answers = []
        count = 15
        while count > 1:
            file_name = f"words/{count}-letter-words.json"
            answers.extend(check_file(file_name, array, answers))
            count = count - 1
        
        # threads = []
        # for n in range(15, 1, -1):
        #     file_name = f"words/{n}-letter-words.json"
        #     t = Thread(target=check_file, args=(file_name, array, answers))
        #     threads.append(t)
        #     t.start()

        # for t in threads:
        #     t.join()
        #     print(t.value)

        post = True
        return render_template("index.html", answers=answers,
                               post=post,
                               letters_array=letters_array)
    return render_template("index.html")

def get_array(array, letters_array):
    counter = 1
    for _ in range(5):
        temp_array = []
        for _ in range(5):
            letter = (request.form.get(f"{counter}")).lower()
            temp_array.append(letter)
            letter = letter.upper()
            letters_array.append(letter)
            counter += 1
        array.append(temp_array)

def check_file(file_name, array, answers):
    check_list = []
    with open(file_name, encoding="utf-8") as file:
        words = json.load(file)
        for word in words:
            checked_word = check_word(word['word'], array)
            if checked_word is not None:
                check_list.append(checked_word)
    return check_list

def check_word(word, array):
    word_array = []
    for letter in word:
        word_array.extend(letter)
    row_number = 0
    while row_number < 5:
        column_number = 0
        for letter in array[row_number]:
            words_letter_number = [0]
            if letter == word_array[0]:
                # create locations[i] lists
                for i in range(20):
                    globals()[f'locations{i}'] = []
                # create records[i] lists - track already used letters
                for i in range(20):
                    globals()[f'records{i}'] = []
                globals()[f'locations{words_letter_number[-1]}'] = [[row_number, column_number]]
                # row and column are numbers showing locations of letters around checked letter
                while True:
                    if len(globals()[f'locations{words_letter_number[-1]}']) > 0:
                        for row in range(3):
                            for column in range(3):
                                # skip the middle location
                                middle_condition = True
                                if row == 1 and column == 1:
                                    middle_condition = False
                                if (globals()[f'locations{words_letter_number[-1]}'][0][0] + (row - 1)) >= 0 and (globals()[f'locations{words_letter_number[-1]}'][0][0] + (row - 1)) < 5 and (globals()[f'locations{words_letter_number[-1]}'][0][1] + (column - 1)) >= 0 and (globals()[f'locations{words_letter_number[-1]}'][0][1] + (column - 1)) < 5:
                                    if word_array[words_letter_number[-1]+1] == array[globals()[f'locations{words_letter_number[-1]}'][0][0] + (row - 1)][globals()[f'locations{words_letter_number[-1]}'][0][1] + (column - 1)] and middle_condition is True:
                                        # prevent from using previous numbers
                                        previous_condition = True
                                        for i in range(len(words_letter_number) - 1):
                                            if globals()[f'locations{words_letter_number[-1]}'][0][0] + (row - 1) == globals()[f'records{i}'][0][0] and globals()[f'locations{words_letter_number[-1]}'][0][1] + (column - 1) == globals()[f'records{i}'][0][1]:
                                                previous_condition = False
                                        if previous_condition is True:
                                            globals()[f'location{words_letter_number[-1] + 1}'] = []
                                            globals()[f'location{words_letter_number[-1] + 1}'].append(globals()[f'locations{words_letter_number[-1]}'][0][0] + (row - 1))
                                            globals()[f'location{words_letter_number[-1] + 1}'].append(globals()[f'locations{words_letter_number[-1]}'][0][1] + (column - 1))
                                            globals()[f'locations{words_letter_number[-1] + 1}'].append(globals()[f'location{words_letter_number[-1] + 1}'])
                    if len(globals()[f'locations{words_letter_number[-1]}']) > 0:
                        record = globals()[f'locations{words_letter_number[-1]}'].copy()
                        globals()[f'records{words_letter_number[-1]}'].insert(0, record[0])
                        globals()[f'locations{words_letter_number[-1]}'].pop(0)
                    if len(globals()[f'locations{words_letter_number[-1] + 1}']) > 0:
                        words_letter_number.append(words_letter_number[-1] + 1)
                    if len(globals()[f'locations{words_letter_number[-1]}']) == 0:
                        words_letter_number.pop()
                    if len(words_letter_number) == 0:
                        break
                    if len(words_letter_number) == len(word_array):
                        record = globals()[f'locations{words_letter_number[-1]}'].copy()
                        globals()[f'records{words_letter_number[-1]}'].extend(record)
                        records = []
                        for i in range(len(word_array)):
                            record = globals()[f'records{i}'][0]
                            # change record to numbers from 1 to 25
                            record = record[0]*5 + record[1] + 1
                            records.append(record)
                        word = word.capitalize()
                        return word, records
            column_number += 1
        row_number += 1

