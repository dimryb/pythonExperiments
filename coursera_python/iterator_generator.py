class MyRangeIterator:
    def __init__(self, top):
        self.top = top
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.top:
            raise StopIteration

        current = self.current
        self.current += 1
        return current


counter = MyRangeIterator(4)
print(counter)

for it in counter:
    print(it)


# Генераторы
def my_range_generator(top):
    current = 0
    while current < top:
        yield current
        current += 1


counter = my_range_generator(3)
print(counter)

for it in counter:
    print(it)
