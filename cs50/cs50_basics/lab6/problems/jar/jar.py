class Jar:
    def __init__(self, capacity=12):
        self.capa = capacity
        self.cookies = 0
        if self.capa < 0 or isinstance(self.capa, int) == False:
            raise ValueError

    def __str__(self):
        return f"{self.cookies} cookies"

    def deposit(self, n):
        self.cookies = self.cookies + n
        if self.cookies > self.capa:
            raise ValueError

    def withdraw(self, n):
        self.cookies = self.cookies - n
        if self.cookies < 0:
            raise ValueError

    @property
    def capacity(self):
        return self.capa

    @property
    def size(self):
        return self.cookies

jar = Jar()
print(str(jar.capacity))
print(str(jar))
jar.deposit(2)
print(str(jar))
jar.withdraw(1)
print(str(jar))
print(jar.capacity)
print(jar.size)