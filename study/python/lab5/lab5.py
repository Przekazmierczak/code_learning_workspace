import math

class RationalNum:
    """
    Opracuj moduł, który będzie definiował klasę, reprezentującą liczby wymierne dodatnie
    w postaci liczby całkowitej i ułamka właściwego.

    Obiekt powinien być tworzony na podstawie trzech informacji: wartości całkowitej
    liczby, licznika części ułamkowej i mianownika części ułamkowej. W obiekcie informacje
    o liczbie powinny być reprezentowane za pomocą liczb całkowitych int.
    """
    def __init__(self, whole, numerator=0, denominator=0):
        # RationalNum(x) create whole numer x
        if not numerator and not denominator:
            whole -= 1
            numerator, denominator = 1, 1

        # RationalNum(x, y) create x/y
        elif not denominator:
            whole, numerator, denominator = 0, whole, numerator

        self.numerator, self.denominator = self.change_to_rational(whole, numerator, denominator)

    def change_to_rational(self, whole, numerator, denominator):
        numerator = numerator + whole * denominator
        gcd = math.gcd(numerator, denominator)
        numerator //= gcd
        denominator = denominator // gcd
        return numerator, denominator

    def __str__(self):
        """
        Wyświetl liczbę w postaci ułamka właściwego.
        """
        whole = self.numerator // self.denominator
        numerator = self.numerator % self.denominator

        if whole and numerator:
            return f"{whole} {numerator}/{self.denominator}"
        elif whole:
            return f"{whole}"
        elif numerator:
            return f"{numerator}/{self.denominator}"
        else:
            return f"0"
    
    def improper_fraction(self):
        """
        Zwróć tekst z liczbą w postaci ułamka niewłaściwego.
        """
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else f"{self.numerator}"
    
    def __repr__(self):
        """
        Zwróć formę reprezentacyjną.
        """
        return f"Rational number: {self.improper_fraction()}"
    
    def __eq__(self, other):
        """
        Porównnaj liczby "==".
        """
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __lt__(self, other):
        """
        Porównnaj liczby "<".
        """
        return self.numerator * other.denominator < other.numerator * self.denominator
    
    def __le__(self, other):
        """
        Porównnaj liczby "<=".
        """
        return self.numerator * other.denominator <= other.numerator * self.denominator
    
    def __gt__(self, other):
        """
        Porównnaj liczby ">".
        """
        return self.numerator * other.denominator > other.numerator * self.denominator
    
    def __ge__(self, other):
        """
        Porównnaj liczby ">=".
        """
        return self.numerator * other.denominator >= other.numerator * self.denominator
    
    def __add__(self, other):
        """
        Zwróć sumę "+".
        """
        if (isinstance(other, int)):
            other = RationalNum(other)

        add_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        add_denominator = self.denominator * other.denominator

        return RationalNum(add_numerator, add_denominator)
    
    def __mul__(self, other):
        """
        Zwróć iloczyn "*".
        """
        if (isinstance(other, int)):
            other = RationalNum(other)

        mul_numerator = self.numerator * other.numerator
        mul_denominator = self.denominator * other.denominator
        return RationalNum(mul_numerator, mul_denominator)
    
    def __truediv__(self, other):
        """
        Zwróć iloraz "/".
        """
        if (isinstance(other, RationalNum)):
            truediv_numerator = self.numerator * other.denominator
            truediv_denominator = self.denominator * other.numerator
        else:
            truediv_numerator = self.numerator
            truediv_denominator = self.denominator * int(other)
        return RationalNum(0, truediv_numerator, truediv_denominator)
    
    def __pow__(self, other):
        """
        Zwróć potegę "**".
        """
        pow_numerator = self.numerator ** other
        pow_denominator = self.denominator ** other
        return RationalNum(0, pow_numerator, pow_denominator)
    
    def __bool__(self):
        """
        Konwertuj do bool "bool()".
        """
        return True if self.numerator != 0 else False
    
    def __float__(self):
        """
        Konwertuj do float "float()".
        """
        return self.numerator / self.denominator

    def __int__(self):
        """
        Konwertuj do int "int()".
        """
        return int(self.numerator / self.denominator)
        
if __name__ == "__main__":
    num1 = RationalNum(2, 3, 6)
    num2 = RationalNum(2, 1, 2)
    num3 = RationalNum(0, 4, 5)
    num4 = RationalNum(8, 0, 3)
    num5 = RationalNum(1, 4, 1)
    num6 = RationalNum(8)
    num7 = RationalNum(1, 4)

    "TEST __str__()"
    assert num1.__str__() == "2 1/2"
    assert num2.__str__() == "2 1/2"
    assert num3.__str__() == "4/5"
    assert num4.__str__() == "8"
    assert num5.__str__() == "5"
    assert num6.__str__() == "8"
    assert num7.__str__() == "1/4"

    "TEST improper_fraction()"
    assert num1.improper_fraction() == "5/2"
    assert num2.improper_fraction() == "5/2"
    assert num3.improper_fraction() == "4/5"
    assert num4.improper_fraction() == "8"
    assert num5.improper_fraction() == "5"
    assert num6.improper_fraction() == "8"
    assert num7.improper_fraction() == "1/4"

    "TEST __repr__()"
    assert num1.__repr__() == "Rational number: 5/2"
    assert num2.__repr__() == "Rational number: 5/2"
    assert num3.__repr__() == "Rational number: 4/5"
    assert num4.__repr__() == "Rational number: 8"
    assert num5.__repr__() == "Rational number: 5"
    assert num6.__repr__() == "Rational number: 8"
    assert num7.__repr__() == "Rational number: 1/4"

    "TEST __eq__()"
    assert num1 == num2
    assert not num1 == num3
    assert not num1 == num4
    assert not num1 == num5
    assert not num3 == num4
    assert not num4 == num5
    assert num4 == num6
    assert not num4 == num7

    "TEST __lt__()"
    assert not num1 < num2
    assert not num1 < num3
    assert num1 < num4
    assert num1 < num5
    assert num3 < num4
    assert not num4 < num5
    assert not num4 < num6
    assert not num4 < num7

    "TEST __le__()"
    assert num1 <= num2
    assert not num1 <= num3
    assert num1 <= num4
    assert num1 <= num5
    assert num3 <= num4
    assert not num4 <= num5
    assert num4 <= num6
    assert not num4 <= num7

    "TEST __gt__()"
    assert not num1 > num2
    assert num1 > num3
    assert not num1 > num4
    assert not num1 > num5
    assert not num3 > num4
    assert num4 > num5
    assert not num4 > num6
    assert num4 > num7

    "TEST __ge__()"
    assert num1 >= num2
    assert num1 >= num3
    assert not num1 >= num4
    assert not num1 >= num5
    assert not num3 >= num4
    assert num4 >= num5
    assert num4 >= num6
    assert num4 >= num7

    "TEST __add__()"
    assert num1 + num2 == RationalNum(5)
    assert num1 + num2 == 5
    assert num1 + num3 == RationalNum(33, 10)
    assert num1 + num4 == RationalNum(10, 1, 2)
    assert num1 + num5 == RationalNum(7, 1, 2)
    assert num3 + num4 == RationalNum(8, 4, 5)
    assert num4 + num5 == 13
    assert num1 + 3 == RationalNum(3, 5, 2)

    "TEST __mul__()"
    assert num1 * num2 == RationalNum(25, 4)
    assert num1 * num3 == RationalNum(2)
    assert num1 * num3 == 2
    assert num1 * num4 == 20
    assert num1 * num5 == RationalNum(25, 2)
    assert num3 * num4 == RationalNum(32, 5)
    assert num4 * num5 == 40

    print("Finished all tests.")