#!/usr/bin/python3
"""script that adds all arguments to a Python list, and then save them to a file"""
import sys
import os.path
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

my_list = []
if os.path.exists("add_item.json") is True:
    my_list = load("add_item.json")
args = sys.argv[1:]
for arg in args:
    my_list.append(arg)
save(my_list, "add_item.json")
