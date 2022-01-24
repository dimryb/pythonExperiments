import os
from to_json import to_json


@to_json
def get_data():
    return {
        'data': 42
    }


@to_json
def get_multi(a, b):
    return a * b


print(get_data.__name__)
print(get_data())  # вернёт '{"data": 42}'
print(get_multi(2, 3))

# os.system("python to_json.py")
