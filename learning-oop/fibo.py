class FibonacciIterator:
    def __init__(self, n):
        self.n=n

    def __iter__(self):
        self.count=0
        self.value=1
        self.prev=0

        return self

    def __next__(self):
        if self.count < self.n:
            value=self.value
            self.value += self.prev
            self.prev=value
            self.count +=1

            return value
        else:
            raise StopIteration


fibo_instance=FibonacciIterator(10)
fibo_iter=iter(fibo_instance)
print(fibo_instance)

for nr in fibo_instance:
    print(nr)

