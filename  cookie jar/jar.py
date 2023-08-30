class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        if self._capacity <=0:raise ValueError
        self.size = 0

    def __str__(self):
        return self.size*str('🍪')

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError

    def withdraw(self, n):
        self.size -= n
        if self.size <=0:
            raise ValueError

    @property
    def capacity(self):
            return self._capacity


    @property
    def size(self):
        return self.size

def main():
    jar = Jar(capacity=20)
    jar.deposit(int(input('Enter number of cookies: ')))
    jar.withdraw(int(input('Enter number of cookies: ')))
    print(jar)

if __name__ == "__main__":
    main()