class Lab1:
    def __init__(self):
        self.tasks = [
            self.task1, self.task2, self.task3,
            self.task4, self.task5, self.task6,
            self.task7, self.task8, self.task9,
            self.task10,
            ]

    def task1(self):
        print("Hello world!")

    def task2(self):
        import math

        x = math.pi/6
        y = math.sin(x)

        print(x)
        print(y)

    def task3(self):
        x = input("Enter your name: ")
        print(f"Hello {x}!")

    def task4(self):
        height = input("Enter your height (in cm): ")
        weight = input("Enter your weight (in kg): ")

        height_m = float(height) / 100
        weight_g = int(weight) * 1000

        print(f"Height: {height_m} m")
        print(f"Weight: {weight_g} g")

    def task5(self):
        import math

        x = float(input("Enter x: "))
        y = float(input("Enter y: "))

        f = math.log(abs(x + 1)) * ((math.sin(x + y) * math.cos(x - y)) / (math.e ** (x ** 2 + y ** 2 + 1)))

        print(f)

    def task6(self):
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        c = int(input("Enter c: "))
        res = 0

        if c == 1:
            res = x + y
        elif c == 2:
            res = x - y
        elif c == 3:
            res = x * y
        else:
            if (y == 0):
                res = "Division by 0!"
            else:
                res = x / y

        print(res)

    def task7(self):
        time = int(input("Enter the time in s: "))

        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time

        print(f"{h}h {m}m {s}s")

    def task8(self):
        text = input("Enter a text: ")
        sign = input("Enter a sign: ")
        count = 0

        for litera in text:
            if litera == sign:
                count += 1

        print(f"Number of signs in the text: {count}")

    def task9(self):
        memo = {}
        def fibb(n):
            if n in memo:
                return memo[n]
            
            if n == 0:
                return 0
            if n <= 2:
                return 1
            
            res = fibb(n - 2) + fibb(n - 1)
            memo[n] = res

            return res


        n = int(input("Enter n: "))
        print(fibb(n))
        
    def task10(self):
        import math

        n = int(input("Enter n: "))

        def if_prime(n):
            if n == 1:
                return False

            for i in range(2, int(math.sqrt(n) + 1)):
                if not n % i:
                    return False
            return True

        print(if_prime(n))

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