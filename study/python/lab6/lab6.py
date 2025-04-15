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
        Napisz funkcję 'copy_file(plik)', która wczyta zawartość pliku z programem o nazwie
        podanej jako parametr i zapisze jego kopię z ponumerowanymi wierszami do nowego pliku.
        """
        def copy_file(file):
            fh_old = None
            fh_new = None
            try:
                fh_old = open(f'{os.getcwd()}/{file}','r',encoding='utf8')
                fh_new = open(f'{os.getcwd()}/{file}_copy','w',encoding='utf8')
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
        Napisz funkcję generującą plik tekstowy z losowo wygenerowaną treścią. Wykorzystaj
        funkcję napisaną na laboratorium nr 4, która generuje losowy ciąg tekstowy o zadanej
        liczbie znaków. Parametry konieczne funkcji : nazwa pliku, liczba znaków. Opcjonalne
        parametry funkcji:
        - minimalna i maksymalna długość słowa,
        - zestaw znaków, z których generowane są słowa,
        - minimalna i maksymalna długość linii.
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
                file_path = os.path.join(os.getcwd(), name)
                fh = open(file_path,'w',encoding='utf8')
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
        Napisz funkcję generującą plik tekstowy z losowo wygenerowaną tabelą wartości numerycznych. 
        Parametry konieczne funkcji : nazwa pliku, liczba kolumn, liczba wierszy. Opcjonalne
        parametry funkcji: zakres wartości jakie przyjmują elementy tabeli. Kolumny w pliku powinny mieć
        jednakową szerokość.
        """
        def randomArray_to_file(name, rows, cols, min=0, max=999):
            fh = None

            # find maximum numer of digits in max possible value 
            digits = 0
            curr_max = max
            while curr_max:
                digits += 1
                curr_max //= 10

            try:
                fh = open(f'{os.getcwd()}/{name}','w',encoding='utf8')
                for _ in range(rows):
                    fh.write("|")
                    for _ in range(cols):
                        fh.write(str(random.randint(min, max)).rjust(digits))
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
        Napisz funkcję, która znajdzie w podanym przez użytkownika katalogu i wszystkich jego
        podkatalogach najstarszy i najnowszy oraz najkrótszy i najdłuższy plik. Funkcja powinna
        zwrócić informacje o znalezionych plikach takie jak: nazwa, ścieżka, długość lub czas
        ostatniej modyfikacji.
        """
        def check_directory(file_path):
            newest = ("", 0)
            oldest = ("", float("inf"))
            largest = ("", 0)
            smallest = ("", float("inf"))

            for path, _, files in os.walk(file_path):
                for file in files:
                    time = os.path.getctime(f'{path}/{str(file)}')
                    size = os.path.getsize(f'{path}/{str(file)}')

                    if time > newest[1]:
                        newest = (file, time)
                    if time < oldest[1]:
                        oldest = (file, time)
                    if size > largest[1]:
                        largest = (file, size)
                    if size < smallest[1]:
                        smallest = (file, size)

            return [
                ("Newest file", newest[0]),
                ("Oldest file", oldest[0]),
                ("Largest file", largest[0]),
                ("Smallest file", smallest[0])
            ]

        print(check_directory(r"C:\Users\elist\Desktop\code_learning_workspace\study\python"))

    def task5(self):
        """
        Napisz funkcję, która znajdzie w podanym przez użytkownika katalogu i wszystkich jego
        podkatalogach wszystkie zdublowane pliki, czyli takie pliki, których nazwa występuje
        jednocześnie w więcej niż jednym miejscu. Funkcja powinna zwrócić listę z nazwami
        dublujących się plików.
        """
        def find_duplicates(file_path):
            names = set()
            duplicates = set()

            for _, _, files in os.walk(file_path):
                for file in files:
                    if file in names:
                        duplicates.add(file)
                    else:
                        names.add(file)
            
            return list(duplicates)
        
        print(find_duplicates(r"C:\Users\elist\Desktop\code_learning_workspace\study\python"))

    def task6(self):
        """
        Napisz funkcję, która znajdzie w podanym przez użytkownika katalogu i wszystkich jego
        podkatalogach wszystkie puste podkatalogi. Funkcja powinna zwrócić listę z ich nazwami.
        """
        def find_empty_directory(file_path):
            empty = []
            for path, directory, files in os.walk(file_path):
                if not directory and not files:
                    empty.append(path.split("\\")[-1])
            
            return empty
        
        print(find_empty_directory(r"C:\Users\elist\Desktop\code_learning_workspace\study\python"))

    def task7(self):
        """
        Napisz funkcję, która znajdzie w podanym przez użytkownika katalogu i wszystkich jego
        podkatalogach wszystkie pliki, które zawierają podany przez użytkownika tekst. Funkcja
        powinna zwrócić listę z nazwami plików.
        """
        def find_file_with_text(file_path, text):
            empty = []
            for path, _, files in os.walk(file_path):
                for file in files:
                    fh = None
                    try:
                        fh = open(f'{path}\{file}','r',encoding='utf8')
                        files_text = fh.read()

                        if text in files_text:
                            empty.append(file)

                    except OSError as err:
                        print('{0}: błąd zapisu: {1}'.format(os.path.basename(sys.argv[0]),err))
                    finally:
                        if fh is not None:
                            fh.close()

            return empty
        
        print(find_file_with_text(r"C:\Users\elist\Desktop\code_learning_workspace\study\python", "test"))

    def task8(self):
        """
        Wczytaj plik tekstowy 'sample_text.txt', w którym zapisany jest przykładowy fragment
        tekstu. Zapisz dane do poprawionego pliku, w którym:
        - usunięte są nadmiarowe spacje,
        - usunięte są spacje przed znakami interpunkcyjnymi,
        - każde zdanie zapisane jest w osobnej linii z numerem na początku,
        - pierwsza litera każdego zdania jest duża.
        """
        def fix_file(name):
            fh_old = None
            fh_new = None
            try:
                fh_old = open(f'{os.getcwd()}/{name}','r',encoding='utf8')
                fh_new = open(f'{os.getcwd()}/fixed_{name}','w',encoding='utf8')
                
                text = fh_old.read()
                text = text.replace("\n", " ")
                words = text.split()
                
                i = 1
                sentence = []
                for word in words:
                    if word not in {".", ",", "!", "?"}:
                        sentence.append(word)
                    else:
                        sentence[-1] = sentence[-1] + word
                    if word[-1] == ("."):
                        fh_new.write(f"{i}. ")
                        curr = " ".join(sentence)
                        fh_new.write(f"{curr.capitalize()}\n")
                        i += 1
                        sentence = []

            except OSError as err:
                print('{0}: błąd zapisu: {1}'.format(os.path.basename(sys.argv[0]),err))
            finally:
                if fh_old is not None:
                    fh_old.close()
                if fh_new is not None:
                    fh_new.close()
        
        fix_file("sample_text.txt")

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