import json

def pretty_print_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(json.dumps(data, indent=4, sort_keys=True))

# Replace 'AboveBelow1.json' with your JSON file path
pretty_print_json('AboveBelow1.json')
