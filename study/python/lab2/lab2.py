import math

class Lab1:
    def __init__(self):
        self.tasks = [
            self.task1, self.task2, self.task3,
            self.task4, self.task5, self.task6,
            self.task7, self.task8
            ]

    def task1(self):
        """
        Napisz funkcję obliczającą w sposób rekurencyjny n-ty wyraz 'Tribonacciego':
            |0 dla n=0
        Fn= |0 dla n=1
            |1 dla n=2
            |Fn-1 + Fn-2 + Fn-3 dla n>2
        """
        def tri(n):
            if n in memo:
                return memo[n]
            
            if n < 2:
                return 0
            if n == 2:
                return 1
            
            res = tri(n - 3) + tri(n - 2) + tri(n - 1)
            memo[n] = res

            return res

        memo = {}
        n = int(input("Enter n: "))
        print(tri(n))

    def task2(self):
        """
        Utwórz krotkę zawierającą 30 elementów: 1,2,...30.
        Wypisz jej zawartość w odwrotnej kolejności.
        Wypisz jej parzyste wartości.
        Wypisz jej wartości, które są liczbami pierwszymi (wykorzystaj funkcję napisaną na poprzednich laboratoriach).
        """
        def is_prime(n):
            if n == 1:
                return False

            for i in range(2, int(math.sqrt(n) + 1)):
                if not n % i:
                    return False
            return True
        
        arr = [i for i in range(1, 31)]
        tup = tuple(arr)

        print("Reversed element:")
        print(str([num for num in reversed(tup)])[1:-1])

        print("Odd elements:")
        print(str([num for num in tup if not num % 2])[1:-1])

        print("Prime elements:")
        print(str([num for num in tup if is_prime(num)])[1:-1])

    def task3(self):
        """
        Za pomocą list, utwórz macierz:
        1   2  3  4
        5   6  7  8
        9  10 11 12
        13 14 15 16
        Utwórz i wyświetl dwie listy zawierające elementy z obu przekątnych macierzy.
        """
        size = 4
        arr = [[row * size + col + 1 for col in range(size)] for row in range(size)]

        diagonal1 = []
        diagonal2 = []

        for i in range(size):
            diagonal1.append(arr[i][i])
            diagonal2.append(arr[i][size - 1 - i])

        print(f"First diagonal: {diagonal1}")
        print(f"Second diagonal: {diagonal2}")

    def task4(self):
        """
        Napisz funkcję wyznaczającą wartość poniższego wzoru, posiadającą dwa opcjonalne parametry:
        stopień logarytmu - domyślnie n=10, wykładnik potęgi - domyślnie k=2.
        f(x,n,k)=logn(x+5)·x^k.
        Oblicz wartości funkcji dla x zmieniającego się w przedziale [-2,2] z krokiem 0.1 i zapisz je w liście.
        """
        def my_log(n = 10, k = 2):
            res = []
            for x in range(-20, 21):
                x /= 10
                res.append(math.log(x + 5, n) * (x ** k))
            return res
        
        print(my_log())

    def task5(self):
        """
        Nie wykorzystując pętli, wypełnij listę nie parzystymi wartościami od 1 do 99. Następnie
        wykonaj kopię listy. W celu sprawdzenia czy kopia została wykonana prawidłowo, zmień
        dowolną wartość w liście oryginalnej i wyświetl obie listy.
        """
        arr = list(range(1, 100, 2))
        arr_copy = arr.copy()
        arr[1] = 999

        print(f"Original array:{arr}")
        print(f"Copied array: {arr_copy}")

    def task6(self):
        """
        Napisz funkcję 'analizujProstokat', do której jako argumenty przekazujemy dwie krotki
        ze współrzędnymi (x,y) lewego-górnego i prawego-dolnego narożnika. Funkcja powinna
        obliczyć i zwrócić obwód i pole powierzchni prostokąta.
        """
        def analizujProstokat(p1, p2):
            side1 = abs(p2[0] - p1[0])
            side2 = abs(p1[1] - p2[1])

            return (f"parimeter: {(side1 + side2) * 2}, area: {side1 * side2}")
        
        print(analizujProstokat((1,4), (3,2)))

    def task7(self):
        """
        Napisz funkcję usuwającą nadmiarowe (podwójne, potrójne, itd.) spacje z tekstu przekazanego
        do niej jako argument. Funkcja powinna zwracać poprawiony tekst.
        Przydatne metody: strip(), replace(t1,t2).
        """
        def fixString(text):
            return " ".join(text.split())

        print(fixString(" test test  test   test    test   "))


    def task8(self):
        """
        Utwórz trzy zbiory:
        A = {1,2,3,4,5}
        B = {2,4,5}
        C = {3,4,5,6,7,8}
        Korzystając z metod zdefiniowanych dla zbiorów, wyznacz i wyświetl:
        - część wspólną zbiorów A i C,
        - sumę zbiorów A i C,
        - różnicę zbiorów A i B,
        - różnicę symetryczną zbiorów A i C
        Zbadaj czy zbiór B jest podzbiorem zbiorów A i C. Wyświetl wynik badania.
        """
        a = {1, 2, 3, 4, 5}
        b = {2, 4, 5}
        c = {3, 4, 5, 6, 7, 8}

        print("intersection:", a & c)
        print("union:", a | c)
        print("difference:", a - b)
        print("symmetric difference:", a ^ b)
        print("is B subset of A:", b.issubset(a))
        print("is B subset of c:", b.issubset(c))


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