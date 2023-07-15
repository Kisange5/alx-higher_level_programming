#!/usr/bin/python3
"""module documentation"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
try:
    old_args = load_from_json_file(filename)
except FileNotFoundError:
    old_args = []
old_args.extend(sys.argv[1:])
save_to_json_file(old_args, filename)
