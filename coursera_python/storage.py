import os
import tempfile
import json
import argparse


def read_json_file(storage_path):
    with open(storage_path, 'r+') as f:
        raw_data = json.load(f)
        data = json.loads(raw_data)
        return data


def write_json_file(storage_path, data):
    with open(storage_path, 'w') as f:
        json.dump(data, f)


def write_key(storage_path, key, val):
    if os.path.exists(storage_path):
        data = read_json_file(storage_path)
        if key in data:
            data[key].append(val)
        else:
            data[key] = [val]
    else:
        data = {key: [val]}

    json_data = json.dumps(data)
    write_json_file(storage_path, json_data)


def read_key(storage_path, key):
    if os.path.exists(storage_path):
        data = read_json_file(storage_path)
        if key in data:
            values = data[key]
            str_values = ""
            for value in values:
                str_values += value + ', '
            print(str_values[:-2])
        else:
            print("None")
    else:
        print("None")


def main(storage_path):
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--val")
    args = parser.parse_args()

    if args.key:
        if args.val:
            write_key(storage_path, args.key, args.val)
        else:
            read_key(storage_path, args.key)


print("storage.py")


if __name__ == '__main__':
    g_storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(g_storage_path)
