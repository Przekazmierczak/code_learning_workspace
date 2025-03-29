import math

class Lab1:
    def __init__(self):
        self.tasks = [
            self.task1, self.task2, self.task3,
            self.task4, self.task5, self.task6,
            self.task7, self.task8
            ]

    def task1(self):
        def check_instance(argument):
            print(f"Number of elements in {type(argument)}: {len(argument)}")
            if isinstance(argument, list): 
                for num, element in enumerate(argument):
                    print(f"Element {num + 1}: {element} is type: {type(element)}")

            if isinstance(argument, dict):
                for key, val in argument.items():
                    print(f"Element with key {key}: {val} is type: {type(val)}")
            
            if isinstance(argument, set) or isinstance(argument, tuple):
                for element in argument:
                    print(f"Element {element} is type: {type(element)}")
                

        list1 = ["abc", "x", 1, 1.5, (1, 2)]
        dict1 = {"a": "abc", "b": "x", "c": 1, "d": 1.5, "e": (1, 2)}
        set1 = set(["abc", "x", 1, 1.5, (1, 2)])
        tuple1 = ("abc", "x", 1, 1.5, (1, 2))
        check_instance(tuple1)

    def task2(self):
        s = {"Szczecin":{1990:400, 2000:390, 2010:385, 2020:380},
             "Poznań":{1990:550, 2000:560, 2010:565, 2020:570},
             "Wrocław":{1990:700, 2000:690, 2010:705, 2020:710}}
        
        towns = s.keys()
        years = s[list(towns)[0]].keys()

        print("Rok| ", end="")
        for town in towns:
            print(f"{town}|", end="")
        print()
        for year in years:
            print(f"{year}|", end="")
            for town in towns:
                print(f"{s[town][year]}| ", end="")
            print()


    def task3(self):
        def print_num(num):
            str_num = str(num)
            dic_num = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

            for digit in str_num:
                print(f"{dic_num[digit]} ", end="")
            print()
        
        print_num(15329)

    def task4(self):
        text = """
        One of the most popular programming languages used nowadays is called Python. It
        has just become more potent with the addition of a few additional features in its most recent iteration.
        Yet, not everyone is aware of its potency. The goal of this book is to introduce readers to Python programming from scratch.
        You are welcome to learn Python Programming like never before, whether you are a computer science undergraduate or not,
        a school-going programming geek or a beginner. You’ll discover everything there is to know about Python,
        including how to use it for programming, when to employ the much-touted walrus operator and other brand-new features of version 3.11.
        Many solved programs that were used as interview questions at various firms are included in the book.
        Understanding the typical mistakes and how to fix them are covered in a separate chapter.
        The difficult topics have been simplified and expressed in simple terms. Beginners and intermediate readers should read the book.
        """
        print(f"Length: {len(text)}")
        print(f"Unique letters: {len(set(text))}")
        letters = {}
        for letter in text:
            if ord("a") <= ord(letter.lower()) <= ord("z"):
                if letter.lower() not in letters:
                    letters[letter.lower()] = 0
                letters[letter.lower()] += 1
        
        print(list(letters.items()).sort(key=lambda x: x[1]))

    def task5(self):
        pass

    def task6(self):
        pass

    def task7(self):
        pass


    def task8(self):
        pass

    def call_task(self, i):
        if 0 <= i < len(self.tasks):
            self.tasks[i]()
        else:
            print(f"Pick number from 0 to {len(self.tasks)}!")


if __name__ == "__main__":
    lab1 = Lab1()
    while True:
        try:
            task = int(input("Pick a task (0 to exit): "))
            if task:
                lab1.call_task(task - 1) 
            else:
                break
        except ValueError:
            break