import json
import os
import sys


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.decoder.JSONDecodeError:
                return None
    return None


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No path specified')
        exit()

    filepath = sys.argv[1]
    data_from_json = load_data(filepath)
    if data_from_json is None:
        print('Wrong file or path')
        exit()

    pretty_print_json(data_from_json)
