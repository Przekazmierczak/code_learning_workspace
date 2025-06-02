import numpy as np
import matplotlib.pyplot as plt
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
        y1(x) = sin(x) + cos(x), y2(x) = 0.01 · sin(x) · exp(x) y3(x) = cos(x) · ln(|x| + 1)
        dla x ∈ [-2π, 2π]. Pierwsza linia powinna mieć kolor czerwony, druga niebieski,
        a trzecia zielony. Zastosuj także różne style linii. Do wykresu dodaj opisy osi i tytuł.
        """
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y1 = np.sin(x) + np.cos(x)
        y2 = 0.01 * np.sin(x) * np.exp(x)
        y3 = np.cos(x) + np.log(np.abs(x) + 1)

        plt.figure()
        plt.plot(x, y1, color='r', linestyle='solid')
        plt.plot(x, y2, color='b', linestyle='dotted')
        plt.plot(x, y3, color='g', linestyle='dashed')

        plt.show()
        

    def task5(self):
        """
        Napisz progam, który w jednym układzie współrzędnych wykreśli rodzinę funkcji.
        """
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        # for range(1000, 2000, 5)


        # plt.figure()
        # plt.plot(x, y1, color='r', linestyle='solid')

        # plt.show()

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

    def task9(self):
        """
        """
        pass


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