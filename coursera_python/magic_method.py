

class MagicMethod:
    items = list(range(10))

    def __getitem__(self, item):
        return self.items[item]

    def __setitem__(self, key, value):
        self.items[key] = value


magic_method = MagicMethod()

magic_method[3] = 99
print(magic_method[3])

print(range(10))
print(list(range(10)))

list1 = [7, 2, 3, 10]
list2 = [-1, 1, -5, 4, 6]
print(list(map(lambda x, y: x*y, list1, list2)))


