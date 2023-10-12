class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        cookie = "🍪"
        return (f"{cookie}" * self.size)

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity need to be non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("There can't be more cookies in jar than maximum capacity")
        if size < 0:
            raise ValueError("There are not enough cookies in the jar")
        self._size = size

def main():
    ...

if __name__ == "__main__":
    main()