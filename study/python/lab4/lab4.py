import random

class Lab1:
    def __init__(self):
        self.tasks = [
            self.print_task1, self.print_task2, self.print_task3,
            self.print_task4, self.print_task5
            ]

    def task1_randomList(self, n, type='int', letters='abcdef', max_len=10, min_val=0, max_val=10):
        """
        Napisz funkcję, która generuje losową listę o zadanej liczbie elementów (parametr
        konieczny). Opcjonalne parametry funkcji:
        - typ elementów (np. int, float, str, mieszany),
        - zestaw znaków, z których generowane są elementy typu str i ich maksymalna długość,
        - zakres wartości jakie przyjmują elementy typu: int, float.
        """
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

    def task2_randomTuple(self, n, type='int', letters='abcdef', max_len=10, min_val=0, max_val=10):
        """
        Napisz funkcję, która generuje losową krotkę o zadanej liczbie elementów (parametr
        konieczny). Opcjonalne parametry funkcji:
        - typ elementów (np. int, float, str, mieszany),
        - zestaw znaków, z których generowane są elementy typu str i ich maksymalna długość,
        - zakres wartości jakie przyjmują elementy typu: int, float.
        """
        return tuple(self.task1_randomList(n, type, letters, max_len, min_val, max_val))
    

    def task3_randomSet(self, n, type='int', letters='abcdef', max_len=10, min_val=0, max_val=10):
        """
        Napisz funkcję, która generuje losowy zbiór o zadanej liczbie elementów (parametr
        konieczny). Opcjonalne parametry funkcji:
        - typ elementów (np. int, float, str, mieszany),
        - zestaw znaków, z których generowane są elementy typu str i ich maksymalna długość,
        - zakres wartości jakie przyjmują elementy typu: int, float.
        """
        return set(self.task1_randomList(n, type, letters, max_len, min_val, max_val))
    
    def task4_randomDict(self, n, key='int', type='int', letters='abcdef', max_len=10, min_val=0, max_val=10):
        """
        Napisz funkcję, która generuje losowy słownik o zadanej liczbie elementów (parametr
        konieczny). Opcjonalne parametry funkcji:
        - typ klucza, np: litery lub wartości int,
        - typ wartości elementów słownika (np. int, float, str, mieszany),
        - zestaw znaków, z których generowane są wartości elementów typu str i ich maksymalna długość,
        - zakres jaki przyjmują wartości elementów typu: int, float.
        """
        # For integer keys
        keys = range(1, n + 1)

        # For string keys
        if key == 'str':
            keys = list(keys)
            # Generate string keys like 'a', 'b', ..., 'aa', 'ab', ..., 'aaa'
            for i, key in enumerate(keys):
                curr_key = []
                while key > 0:
                    key -= 1
                    curr_key.append(chr((key % 26) + ord('a')))
                    key //= 26
                keys[i] = "".join(curr_key[::-1])

        return dict(zip(keys, self.task1_randomList(n, type, letters, max_len, min_val, max_val)))
    
    def task5_randomText(self, n, min_word=3, max_word=10, characters='abcdef', min_line=20, max_line=40):
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
    
    # Print tasks (test)
    def print_task1(self):
        n = int(input("Insert n: "))
        print(self.task1_randomList(n, type='mix'))

    def print_task2(self):
        n = int(input("Insert n: "))
        print(self.task2_randomTuple(n, type='mix'))

    def print_task3(self):
        n = int(input("Insert n: "))
        print(self.task3_randomSet(n, type='mix'))

    def print_task4(self):
        n = int(input("Insert n: "))
        print(self.task4_randomDict(n, key='str', type='mix'))

    def print_task5(self):
        n = int(input("Insert n: "))
        print(self.task5_randomText(n))

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