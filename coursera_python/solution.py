import os
import tempfile


class File:
    def __init__(self, path_name):
        self.path_name = path_name
        if not os.path.exists(path_name):
            with open(path_name, 'w') as f:
                f.write("")

    def read(self):
        with open(self.path_name, 'r') as f:
            data = f.read()
            return data

    def write(self, text):
        with open(self.path_name, 'w') as f:
            return f.write(text)

    def __add__(self, other):
        data = self.read()
        new_data = data + other.read()
        random_name = tempfile.NamedTemporaryFile().name
        path_new_file = os.path.join(os.path.abspath(tempfile.gettempdir()), random_name)
        new_file = File(path_new_file)
        new_file.write(new_data)
        return new_file

    def __str__(self):
        return self.path_name

    def __iter__(self):
        with open(self.path_name, 'r') as f:
            self.read_lines = f.read().splitlines()
        self.current_iter = 0
        self.end_iter = len(self.read_lines)
        return self

    def __next__(self):
        if self.current_iter >= self.end_iter:
            raise StopIteration
        result = self.read_lines[self.current_iter]+'\n'
        self.current_iter += 1
        return result
