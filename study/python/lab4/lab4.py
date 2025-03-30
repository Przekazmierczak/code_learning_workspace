import math
import random

class Lab1:
    def __init__(self):
        self.tasks = [
            self.task1, self.task2, self.task3,
            self.task4, self.task5, self.task6,
            self.task7, self.task8
            ]

    def task1(self):
        def randomList(n, type='int', letters='abcdef', max_len=10, min_val=0, max_val=10):
            array = []
            if_mix = False if type != 'mix' else True
            types = ['int', 'float', 'str']

            for _ in range(n):
                if if_mix:
                    type = types[random.randint(0, 2)]
                if type == 'int':
                    array.append(random.randint(min_val,max_val))
                elif type == 'float':
                    array.append(random.randint(min_val,max_val - 1) + random.random())
                elif type == 'str':
                    array.append("".join(random.choices(letters, k=random.randint(1, max_len))))

            return array
        
        def randomTuple(n, type='int', letters='abcdef', max_len=10, min_val=0, max_val=10):
            return tuple(randomList(n, type, letters, max_len, min_val, max_val))
        
        def randomSet(n, type='int', letters='abcdef', max_len=10, min_val=0, max_val=10):
            return set(randomList(n, type, letters, max_len, min_val, max_val))

        def randomDict(n, key='int', type='int', letters='abcdef', max_len=10, min_val=0, max_val=10):
            keys = range(n)
            if key == 'char':
                keys  = range(n)
            return dict(zip(keys, randomList(n, type, letters, max_len, min_val, max_val)))
        
        def randomText(n, min_word=1, max_word=10, letters='abcdef', line=5):
            text = []
            word_in_line = 0
            while n >= 0:
                curr_word = random.randint(min_word, max_word)
                for _ in range(curr_word):
                    text.append(random.choice(letters))
                    n -= 1
                    if n < 0:
                        return "".join(text)
                text.append(" ")
                n -= 1
                word_in_line += 1
                if word_in_line == line:
                    text.append("\n")
                    word_in_line = 0
            return "".join(text)
                
        
        # print(randomList(10, type='mix'))
        # print(randomTuple(10, type='mix'))
        # print(randomSet(10, type='mix'))
        # print(randomDict(10, type='mix'))
        print(randomText(300))

    def task2(self):
        pass

    def task3(self):
        pass

    def task4(self):
        pass

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