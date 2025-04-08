import math

class Lab1:
    def __init__(self):
        self.tasks = [
            self.task1
            ]

    def task1(self):
        class RationalNum:
            def __init__(self, intig, numerator, denominator):
                self.input_intig = intig
                self.input_numerator = numerator
                self.input_denominator = denominator
                self.numerator, self.denominator = self.reduce()

            def reduce(self):
                numerator = self.input_numerator + self.input_intig * self.input_denominator
                common_deno = math.gcd(numerator, self.input_denominator)
                numerator //= common_deno
                denominator = self.input_denominator // common_deno
                return numerator, denominator

            def __str__(self):
                return f"{self.input_intig} {self.input_numerator}/{self.input_denominator}"
            
            def print(self):
                return f"{self.numerator}/{self.denominator}"
            
            def __repr__(self):
                return f"Rational number: {self.numerator} / {self.denominator}"
            
            def __eq__(self, other):
                return self.numerator == other.numerator and self.denominator == other.denominator
            
            def __lt__(self, other):
                return self.numerator * other.denominator < other.numerator * self.denominator
            
            def __le__(self, other):
                return self.numerator * other.denominator <= other.numerator * self.denominator
            
            def __gt__(self, other):
                return self.numerator * other.denominator > other.numerator * self.denominator
            
            def __ge__(self, other):
                return self.numerator * other.denominator >= other.numerator * self.denominator
            
            def __add__(self, other):
                if (isinstance(other, RationalNum)):
                    add_numerator = self.numerator * other.denominator + self.denominator * self.numerator
                    add_denominator = self.denominator * other.denominator
                else:
                    add_numerator = self.numerator + int(other) * self.denominator
                    add_denominator = self.denominator
                return RationalNum(0, add_numerator, add_denominator)
            
            def __mul__(self, other):
                if (isinstance(other, RationalNum)):
                    mull_numerator = self.numerator * other.numerator
                    mull_denominator = self.denominator * other.denominator
                else:
                    mull_numerator = self.numerator * int(other)
                    mull_denominator = self.denominator
                return RationalNum(0, mull_numerator, mull_denominator)
            
            def __truediv__(self, other):
                if (isinstance(other, RationalNum)):
                    truediv_numerator = self.numerator * other.denominator
                    truediv_denominator = self.denominator * other.numerator
                else:
                    truediv_numerator = self.numerator
                    truediv_denominator = self.denominator * int(other)
                return RationalNum(0, truediv_numerator, truediv_denominator)
            
            def __pow__(self, other):
                pow_numerator = self.numerator ** other
                pow_denominator = self.denominator ** other
                return RationalNum(0, pow_numerator, pow_denominator)
            
            def __bool__(self):
                return True if self.numerator != 0 else False
            
            def __float__(self):
                return self.numerator / self.denominator

            def __int__(self):
                return int(self.numerator / self.denominator)
                

        num = RationalNum(2, 3, 6)
        other = RationalNum(2, 1, 3)
        other2 = RationalNum(0, 5, 2)
        print(num)
        num.print()
        assert bool(num) == True
        assert bool(RationalNum(0, 0, 5) == False)
        print(int(num))



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