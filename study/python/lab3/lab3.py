class Lab1:
    def __init__(self):
        self.tasks = [
            self.task1, self.task2, self.task3,
            self.task4, self.task5,
            ]

    def task1(self):
        """
        Napisz funkcję, której argumentem może być krotka, lista, zbiór lub słownik. Funkcja
        powinna wyświetlać informacje o przekazanym obiekcie.
        """
        def check_instance(argument):
            print(f"Number of elements in {str(type(argument))[8:-2]}: {len(argument)}")
            if isinstance(argument, list): 
                for num, element in enumerate(argument):
                    print(f"Element {num + 1}: {element} is type: {str(type(element))[8:-2]}")

            if isinstance(argument, dict):
                for key, val in argument.items():
                    print(f"Element with key {key}: {val} is type: {str(type(val))[8:-2]}")
            
            if isinstance(argument, set) or isinstance(argument, tuple):
                for element in argument:
                    print(f"Element {element} is type: {str(type(element))[8:-2]}")
                

        list1 = ["abc", "x", 1, 1.5, (1, 2)]
        dict1 = {"a": "abc", "b": "x", "c": 1, "d": 1.5, "e": (1, 2)}
        set1 = set(["abc", "x", 1, 1.5, (1, 2)])
        tuple1 = ("abc", "x", 1, 1.5, (1, 2))
        check_instance(set1)

    def task2(self):
        """
        Napisz program, który dla słownika:
        S = {
        'Szczecin':{1990:400, 2000:390, 2010:385, 2020:380},
        'Poznań':{1990:550, 2000:560, 2010:565, 2020:570},
        'Wrocław':{1990:700, 2000:690, 2010:705, 2020:710},
        }
        wyświetli jego zawartość w formie tabeli:
        Rok | Szczecin | Poznań | Wrocław |
        -----------------------------------
        1990 |     400 |    550 |     700 |
        2000 |     390 |    560 |     690 |
        2010 |     385 |    565 |     705 |
        2020 |     380 |    570 |     710 |
        -----------------------------------
        """
        s = {"Szczecin":{1990:400, 2000:390, 2010:385, 2020:380},
             "Poznań":{1990:550, 2000:560, 2010:565, 2020:570},
             "Wrocław":{1990:700, 2000:690, 2010:705, 2020:710}}
        
        # Check for the longest position to set the column width
        longest = 0
        for key, value in s.items():
            longest = max(longest, len(str(key)))
            for key_val, val_val in value.items():
                longest = (max(longest, len(str(key_val)), len(str(val_val))))
        longest += 1

        towns = s.keys()
        years = s[next(iter(s))].keys()
        years_len = 5

        # Print the first row
        print("Rok|".rjust(years_len), end="")
        for town in towns:
            print(f"{town}|".rjust(longest), end="")
        print()

        print("".join(["-" for _ in range(years_len + longest * len(towns))]))

        # Print the rest rows
        for year in years:
            print(f"{year}|".rjust(years_len), end="")
            for town in towns:
                print(f"{s[town][year]}|".rjust(longest), end="")
            print()

        # Print the last row
        print("".join(["-" for _ in range(years_len + longest * len(towns))]))

    def task3(self):
        """
        Wykorzystując słownik, napisz funkcję, która zwróci słowną reprezentację liczby
        całkowitej przekazanej jako argument, np:
        135 → 'jeden trzy pięć'
        """
        def int_to_str(num):
            dic_num = {"0": "zero", "1": "one", "2": "two",
                       "3": "three", "4": "four", "5": "five",
                       "6": "six", "7": "seven", "8": "eight", "9": "nine"}
            return " ".join([dic_num[digit] for digit in str(num)])
        
        print(int_to_str(15329))

    def task4(self):
        """
        Wynacz długość tekstu i określ ile jest unikalnych liter w tekście. Wyznacz częstość
        występowania poszczególnych liter (nie bierz pod uwagę spacji, znaków interpunkcyjnych,
        cyfr i znaków nowego wiersza). Zignoruj także wielkość liter. Wyświetl je w kolejności od
        najczęstszej do wystepującej najrzadziej.
        Ile jest wszystkich wyrazów, a ile jest wyrazów unikalnych? Wyznacz częstość wystę
        powania poszczególnych wyrazów w tekście. Wyświetl je w kolejności od najczęstszych do
        wystepujących najrzadziej
        """
        text = """
        One of the most popular programming languages used nowadays is called Python. It
        has just become more potent with the addition of a few additional features in its
        most recent iteration. Yet, not everyone is aware of its potency. The goal of this book
        is to introduce readers to Python programming from scratch. You are welcome to learn Python
        Programming like never before, whether you are a computer science undergraduate or not,
        a school-going programming geek or a beginner. You'll discover everything there is to know
        about Python, including how to use it for programming, when to employ the much-touted walrus
        operator and other brand-new features of version 3.11. Many solved programs that were used as
        interview questions at various firms are included in the book. Understanding the typical
        mistakes and how to fix them are covered in a separate chapter. The difficult topics have been
        simplified and expressed in simple terms. Beginners and intermediate readers should read the book.
        """
        # Text length
        print(f"Length: {len(text)}")
        # Number of unique letters
        print(f"Unique letters: {len(set(text))}")

        # Frequency of letters
        letters = {}
        for letter in text:
            if ord("a") <= ord(letter.lower()) <= ord("z"):
                if letter.lower() not in letters:
                    letters[letter.lower()] = 0
                letters[letter.lower()] += 1
        freq_letters = (sorted(list(letters.items()), key=lambda x: x[1], reverse=True))

        print("Frequency of letters:")
        for letter, num in freq_letters:
            print(f"{letter}: {num}, ", end="")
        print()

        # Number of words
        words = text.lower().split()
        print(f"Number of words: {len(words)}")

        # Remove interpunction at the end of the word, but keep the one inside the word like in 3.11 or brand-new
        for i, word in enumerate(words):
            if  not word[-1].isalpha() and not word[-1].isnumeric():
                words[i] = word[:-1]

        # Number of unique words
        set_words = set(words)
        print(f"Number of unique words: {len(set_words)}")

        # Frequency of words
        words_dic = {}
        for word in words:
            if word not in words_dic:
                words_dic[word] = 0
            words_dic[word] += 1
        freq_words = (sorted(list(words_dic.items()), key=lambda x: x[1], reverse=True))

        print("Frequency of words:")
        for word, num in freq_words:
            print(f"{word}: {num}, ", end="")
        print()

    def task5(self):
        """
        Napisz funkcję, która dla dwóch ciągów tekstowych wyznacza tzw. odległość Levenshteina,
        zdefiniowaną następująco:

        działaniem prostym na ciągu tekstowym nazwiemy:
        - wstawienie nowego znaku do ciągu,
        - usunięcie znaku z ciagu,
        - zamianę znaku w ciągu na inny znak,

        odległością pomiędzy dwoma ciągami tekstowymi jest najmniejsza liczba działań
        prostych, przeprowadzających jeden ciąg w drugi.

        Jaka jest odległość między słowami kot i kocioł?
        """
        def minDist(i1, i2, word1, word2, memo):
            # Need to insert remaining characters
            if i1 == len(word1):
                return len(word2) - i2
            
            # Need to delete remaining characters
            if i2 == len(word2):
                return len(word1) - i1
            
            # Check if the current pair is already memoized
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            
            # Move to the next pair
            if word1[i1] == word2[i2]:
                return minDist(i1 + 1, i2 + 1, word1, word2, memo)
            
            # Recursive calls for the three basic operations
            res = 1 + min(minDist(i1 + 1, i2, word1, word2, memo), # Insert
                          minDist(i1, i2 + 1, word1, word2, memo), # Delete
                          minDist(i1 + 1, i2 + 1, word1, word2, memo)) # Replace

            # Memoization
            memo[(i1, i2)] = res

            return res

        word1 = "kot"
        word2 = "kocioł"

        memo = {}

        print(minDist(0, 0, word1, word2, memo))

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