import time


class timer():
    def __init__(self):
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print('Elapsed: {}'.format(self.current_time()))

    def __repr__(self):
        return "<Класс таймера>"

    def __str__(self):
        return "Класс таймера"

    def __getattr__(self, item):
        return "Такого атрибута нет: {}".format(item)


with timer() as t:
    #time.sleep(1)
    print('Current: {}'.format(t.current_time()))
    #time.sleep(1)

t = timer()
print(t.__repr__())
print(t.__str__())

print(type(t))

print(t.not_attrib)
print(t.__dir__())
print(t)
