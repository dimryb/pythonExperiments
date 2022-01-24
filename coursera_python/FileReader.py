
class FileReader:

    def __init__(self, path_name):
        self._path_name = path_name

    def read(self):
        try:
            with open(self._path_name, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            data = ""
            return data

