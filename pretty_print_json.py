"""
This module provides functionality to pretty print JSON data from a file.

Functions:
    - pretty_print_json(file_path): Reads JSON data from a specified file and prints it in a formatted manner.
"""

import json

def pretty_print_json(file_path):
    """
    Reads JSON data from a specified file and prints it in a formatted manner.

    Args:
        file_path (str): The path to the JSON file to be read.

    Example:
        pretty_print_json('path/to/your/file.json')
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(json.dumps(data, indent=4, sort_keys=True))

# Replace 'AboveBelow1.json' with your JSON file path
pretty_print_json('AboveBelow1.json')
