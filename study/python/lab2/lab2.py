import math

class Lab1:
    def __init__(self):
        self.tasks = [
            self.task1, self.task2, self.task3,
            self.task4, self.task5, self.task6,
            self.task7, self.task8
            ]

    def task1(self):
        memo = {}
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

        n = int(input("Enter n: "))
        print(tri(n))

    def task2(self):
        def is_prime(n):
            if n == 1:
                return False

            for i in range(2, int(math.sqrt(n) + 1)):
                if not n % i:
                    return False
            return True
        
        arr = []
        for i in range(1, 31):
            arr.append(i)

        tup = tuple(arr)

        print("Reversed element:")
        for num in reversed(tup):
            print(num, end=", ")
        print()

        print("Odd elements:")
        for num in tup:
            if not num % 2:
                print(num, end=", ")
        print()

        print("Prime elements:")
        for num in tup:
            if is_prime(num):
                print(num, end=", ")
        print()


    def task3(self):
        size = 4
        arr = []

        for row in range (size):
            inner = []
            for col in range(size):
                inner.append(row * size + col + 1)
            arr.append(inner)

        list1 = []
        for i in range(size):
            list1.append(arr[i][i])

        list2 = []
        for i in reversed(range(size)):
            list2.append(arr[i][i])
        
        print(list1)
        print(list2)  

    def task4(self):
        def my_log(n, k):
            res = []
            for x in range(-20, 20):
                x /= 10
                res.append(round(math.log(x + 5, n) * (x ** k), 4))
            return res
        
        print(my_log(10, 2))

    def task5(self):
        arr = list(range(1, 99, 2))

        arr_copy = arr.copy()
        print("Array before:")
        print(arr_copy)

        arr_copy[10] = 999
        print("Array after:")
        print(arr_copy)

    def task6(self):
        def analizujProstokat(p1, p2):
            pari = (p2[0] - p1[0] + p1[1] - p2[1]) * 2
            area = (p2[0] - p1[0]) * (p1[1] - p2[1])
            return (pari, area)
        
        print(analizujProstokat((1,4), (3,2)))

    def task7(self):
        def fixString(text):
            array = text.split(" ")

            array2 = []
            for word in array:
                if word:
                    array2.append(word)

            return " ".join(array2)
    
        print(fixString(" test test  test   test    test" ))


    def task8(self):
        a = {1, 2, 3, 4, 5}
        b = {2, 4, 5}
        c = {3, 4, 5, 6, 7, 8}

        difference = (a - b)
        union = a | c
        intersection = (a & c)

        print("difference", difference)
        print("union", union)
        print("intersection", intersection)


    def call_task(self, i):
        if 0 <= i < len(self.tasks):
            self.tasks[i]()
        else:
            print(f"Pick number from 0 to {len(self.tasks)}!")


if __name__ == "__main__":
    lab1 = Lab1()
    while True:
        task = int(input("Pick a task (0 to exit): "))
        if task:
            lab1.call_task(task - 1) 
        else:
            break