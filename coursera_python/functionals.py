def list_int_to_list_str(list_ints):
    list_str = []
    for i in list_ints:
        list_str.append(str(i))
    return list_str


def stringify_list(num_list):
    return list(map(str, num_list))


g_list_ints = [1, 4, 2, 5, 3, 8, 7]

print(list_int_to_list_str(g_list_ints))
print(stringify_list(g_list_ints))
