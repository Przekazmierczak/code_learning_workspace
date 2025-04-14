import os
import sys
import random
import time

class Lab6:
    def __init__(self):
        self.tasks = [
            self.task1, self.task2, self.task3,
            self.task4, self.task5, self.task6,
            self.task7, self.task8
            ]

    def task1(self):
        """
        """
        def copy_file(name):
            fh_old = None
            fh_new = None
            try:
                fh_old = open(f'{os.getcwd()}/{name}','r',encoding='utf8')
                fh_new = open(f'{os.getcwd()}/{name}_copy','w',encoding='utf8')
                text = fh_old.read()

                lines = text.splitlines()

                i = 1
                for line in lines:
                    fh_new.write(f"{i}. ")
                    fh_new.write(f"{line}\n")
                    i += 1

            except OSError as err:
                print('{0}: błąd zapisu: {1}'.format(os.path.basename(sys.argv[0]),err))
            finally:
                if fh_old is not None:
                    fh_old.close()
                if fh_new is not None:
                    fh_new.close()
        
        copy_file("task1_test")

    def task2(self):
        """
        """
        def task5_randomText(n, min_word=3, max_word=10, characters='abcdef', min_line=20, max_line=40):
            """
            Napisz funkcję, która generuje losowy ciąg tekstowy o zadanej liczbie znaków (parametr konieczny).
            Opcjonalne parametry funkcji:
            - minimalna i maksymalna długość słowa,
            - zestaw znaków, z których generowane są słowa,
            - minimalna i maksymalna długość linii.
            """
            text = []
            characters_in_line = random.randint(min_line, max_line)
            curr_word = random.randint(min_word, max_word)

            for _ in range(n):
                text.append(random.choice(characters))
                curr_word -= 1
                characters_in_line -= 1

                if curr_word <= 0:
                    if characters_in_line <= 0:
                        text.append("\n")
                        characters_in_line = random.randint(min_line, max_line)
                    else:
                        text.append(" ")
                    curr_word = random.randint(min_word, max_word)

            return "".join(text)
        
        def randomText_to_file(name, n, min_word=3, max_word=10, characters='abcdef', min_line=20, max_line=40):
            fh = None
            try:
                fh = open(f'{os.getcwd()}/{name}','w',encoding='utf8')
                text = task5_randomText(n, min_word, max_word, characters, min_line, max_line)
                fh.write(text)

            except OSError as err:
                print('{0}: błąd zapisu: {1}'.format(os.path.basename(sys.argv[0]),err))
            finally:
                if fh is not None:
                    fh.close()

        randomText_to_file("task2_test", 100)

    def task3(self):
        """
        """
        def randomArray_to_file(name, rows, cols, min=0, max=999):
            fh = None
            try:
                fh = open(f'{os.getcwd()}/{name}','w',encoding='utf8')
                for _ in range(rows):
                    fh.write("|")
                    for _ in range(cols):
                        fh.write(str(random.randint(min, max)).rjust(4))
                        fh.write("|")
                    fh.write("\n")

            except OSError as err:
                print('{0}: błąd zapisu: {1}'.format(os.path.basename(sys.argv[0]),err))
            finally:
                if fh is not None:
                    fh.close()
        
        randomArray_to_file("task3_test", 8, 7)

    def task4(self):
        """
        """
        print(os.getcwd())
        def check_directory(file_path):
            newest = ("", 0)
            oldest = ("", float("inf"))
            longest = ("", 0)
            shortest = ("", float("inf"))

            for path, directory, files in os.walk(file_path):
                if str(files):
                    for file in files:
                        time = os.path.getctime(f'{path}/{str(file)}')
                        size = os.path.getsize(f'{path}/{str(file)}')

                        if time > newest[1]:
                            newest = (file, time)
                        if time < oldest[1]:
                            oldest = (file, time)
                        if size > longest[1]:
                            longest = (file, size)
                        if size < shortest[1]:
                            shortest = (file, size)

            print(f"newest file: {newest}")
            print(f"oldest file: {oldest}")
            print(f"longest file: {longest}")
            print(f"shortest file: {shortest}")

                        

        check_directory(r"/Users/przemyslawkazmierczak/Desktop/code_learning_workspace/study/python/")

    def task5(self):
        """
        """
        pass

    def task6(self):
        """
        """
        pass

    def task7(self):
        """
        """
        pass

    def task8(self):
        """
        """
        pass

    def call_task(self, i):
        if 0 <= i < len(self.tasks):
            self.tasks[i]()
        else:
            print(f"Pick number from 0 to {len(self.tasks)}!")


if __name__ == "__main__":
    lab6 = Lab6()
    while True:
        try:
            task = int(input("Pick a task (0 to exit): "))
            if task:
                lab6.call_task(task - 1) 
            else:
                break
        except ValueError:
            break