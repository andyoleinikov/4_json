import json
import os
import sys


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as json_file:
            try:
                return json.load(json_file)
            except json.decoder.JSONDecodeError:
                return None
    return None


def pretty_print_json(data_from_json):
    print(json.dumps(data_from_json, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No path specified')

    filepath = sys.argv[1]
    data_from_json = load_data(filepath)
    if data_from_json is None:
        sys.exit('Wrong file or path')

    pretty_print_json(data_from_json)
