import os.path
import tempfile
from solution import File

file_name = 'test.file1'
path_to_file = os.path.join(os.path.abspath(tempfile.gettempdir()), file_name)

if os.path.exists(path_to_file):
    os.remove(path_to_file)
assert (not os.path.exists(path_to_file))

print(tempfile.gettempdir())

file_obj = File(path_to_file)
assert (os.path.exists(path_to_file))
assert (file_obj.read() == '')
assert (9 == file_obj.write('some text'))
assert ('some text' == file_obj.read())
assert (10 == file_obj.write('other text'))
assert ('other text' == file_obj.read())
file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
assert (7 == file_obj_1.write('line 1\n'))
assert (7 == file_obj_2.write('line 2\n'))
new_file_obj = file_obj_1 + file_obj_2
assert (isinstance(new_file_obj, File))
print(new_file_obj)
for line in new_file_obj:
    print(ascii(line))
