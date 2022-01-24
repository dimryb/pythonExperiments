
path_name = 'test.file'
with open(path_name, 'w') as f:
    f.write("test test test")

with open(path_name, 'r') as f:
    data = f.read()
    print(data)