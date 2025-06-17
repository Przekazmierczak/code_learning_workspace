import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

class Lab7:
    def __init__(self):
        self.tasks = [
            self.task1, self.task2, self.task3,
            self.task4, self.task5, self.task6,
            self.task7, self.task8, self.task9
            ]

    def task1(self):
        """
        Utwórz macierze współczynników i rozwiąż układ równań liniowych.
        x1 - 2x2 + x4 = 1
        2x2 + x3 - x4 = 3
        3x1 + 2x4 = 11
        x1 + x2 + x3 + x4 =10
        """
        A = np.array([
            [1, 2, 0, 4],
            [0, 2, 1, -1],
            [3, 0, 0, 2],
            [1, 1, 1, 1]])
        
        b = np.array([1, 3, 11, 10])
        
        x = np.linalg.solve(A, b)

        print("Solution :", x)

    def task2(self):
        """
        Napisz funkcję, do której jako argument przekazujemy liczbę naturalną n.
        Funkcja powinna zwrócić macierz kwadratową o rozmierze n * n,
        w której na przekątnej znajdują się wartości n, powyżej wartości 1, a poniżej -1.
        """
        def create_matrix(n):
            matrix = np.zeros((n, n))
            for row in range(n):
                for col in range(n):
                    if (col < n - 1 - row):
                        matrix[row][col] = 1
                    elif (col > n - 1 - row):
                        matrix[row][col] = -1
                    else:
                        matrix[row][col] = n
            return matrix
        
        print(create_matrix(4))

    def task3(self):
        """
        Napisz progam, który wykreśli wykres funkcji
        """
        x = np.linspace(-5, 5, 100)
        y = (np.sqrt(np.sin(x) + 2))/(np.abs(np.sin(x) + np.cos(x)) + 1)

        plt.figure()
        plt.plot(x, y, 'r')

        plt.show()

    def task4(self):
        """
        Napisz progam, który w jednym układzie współrzędnych wykreśli wykresy 3 funkcji:
        y1(x) = sin(x) + cos(x)
        y2(x) = 0.01 · sin(x) · exp(x)
        y3(x) = cos(x) · ln(|x| + 1)
        dla x ∈ [-2π, 2π].
        Pierwsza linia powinna mieć kolor czerwony, druga niebieski, a trzecia zielony.
        Zastosuj także różne style linii. Do wykresu dodaj opisy osi i tytuł.
        """
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y1 = np.sin(x) + np.cos(x)
        y2 = 0.01 * np.sin(x) * np.exp(x)
        y3 = np.cos(x) + np.log(np.abs(x) + 1)

        plt.figure()
        plt.plot(x, y1, color='r', linestyle='solid')
        plt.plot(x, y2, color='b', linestyle='dotted')
        plt.plot(x, y3, color='g', linestyle='dashed')

        plt.xlabel('x')
        plt.ylabel('Oś y')
        plt.title('Trzy linie')

        plt.show()
        
    def task5(self):
        """
        Napisz progam, który w jednym układzie współrzędnych wykreśli rodzinę funkcji.
        """
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        k = np.arange(1, 2.05, 0.05)

        plt.figure()

        for k_element in k:
            y = np.exp(np.cos(k_element * x) + 1) / (np.abs(x) + 1)
            plt.plot(x, y, color='r', linestyle='solid')
        
        plt.xlabel('x')
        plt.ylabel('Oś y')
        plt.title('K family')

        plt.show()

    def task6(self):
        """
        Napisz progam, który narysuje wykres funkcji 2 zmiennych.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x, y = np.meshgrid(np.linspace(-np.pi/2, np.pi/2, 100), np.linspace(-np.pi/2, np.pi/2, 100))
        z = (np.sin(x * y)**2 + np.cos(x + y)**2) / (np.abs(x) + np.abs(y) + 1)
        ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='jet', alpha=0.8)
        plt.show()

    def task7(self):
        """
        Napisz progam, który narysuje wykres poziomicowy funkcji 2 zmiennych:
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        x, y = np.meshgrid(np.linspace(-2*np.pi, 2*np.pi, 100), np.linspace(-2*np.pi, 2*np.pi, 100))
        z = np.sin(x + y) + np.cos(x - y)
        ax.contour(x, y, z, cmap='jet', alpha=0.8)
        plt.show()

    def task8(self):
        """
        Napisz funkcję, do której jako argument przekazujemy liczbę naturalną n.Funkcja powinna zwrócić macierz kwadratową o rozmierze n x n
        wypełnioną wartościami od 1 do n2. W pierwszym wierszu kolejne liczby rozmieszczone są od lewej do prawej, w drugim
        od prawej do lewej, itd. Przykład dla n=4 poniżej.
        | 1  2  3  4|
        | 8  7  6  5|
        | 9 10 11 12|
        |16 15 14 13|
        """
        def weird_matrix(n):
            matrix = np.arange(1, n**2 + 1)
            matrix = matrix.reshape(n, n)
            for i in range(1, n, 2):
                matrix[i] = matrix[i][::-1]
            return matrix
        
        print(weird_matrix(10))

    def task9(self):
        """
        Wczytaj dane z pliku tekstowego dane_lab_7.txt do macierzy.
        M = np.loadtxt('dane_lab_7.txt')
        - Określ ile jest wierszy i kolumn.
        - Jaka jest najmniejsza, największa i średnia wartość w każdej kolumnie?
        - Wykreśl wykres punktowy pokazujący zależność wartości w 2 i 3 kolumnie. Zapisz
        wykres do pliku (metoda savefig()).
        - Wykreśl w jednym oknie wykresy punktowe pokazujące wzajemne zależności pomiędzy
        wszystkimi kolumnami (polecenie subplot()) - patrz rysunek poniżej.
        """
        M = np.loadtxt('dane_lab_7.txt')

        rows, cols = M.shape
        print(f"Liczba wierszy: {rows}")
        print(f"Liczba kolumn: {cols}")

        min_values = np.min(M, axis=0)
        max_values = np.max(M, axis=0)
        mean_values = np.mean(M, axis=0)

        for i in range(4):
            print(f"Kolumna nr. {i + 1}:")
            print(f"Minimana wartość: {min_values[i]}")
            print(f"Maksymalna wartość: {max_values[i]}")
            print(f"Średnia wartość: {mean_values[i]}")
        
        fig = plt.figure(num=1)
        ax = fig.add_subplot(1,1,1)
        ax.scatter(M[:, 1], M[:, 2], color='r')
        fig.savefig('scatter.pdf', bbox_inches='tight', dpi=600)

        plt.figure()
        for i in range(4):
            for j in range(4):
                plt.subplot(4,4, i * 4 + j + 1)
                plt.scatter(M[:, i], M[:, j], color='r')

        plt.show()

    def call_task(self, i):
        if 0 <= i < len(self.tasks):
            self.tasks[i]()
        else:
            print(f"Pick number from 0 to {len(self.tasks)}!")


if __name__ == "__main__":
    lab7 = Lab7()
    while True:
        try:
            task = int(input("Pick a task (0 to exit): "))
            if task:
                lab7.call_task(task - 1) 
            else:
                break
        except ValueError:
            break