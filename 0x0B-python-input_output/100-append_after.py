#!/usr/bin/python3

"""append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string"""
    with open(filename, "r", encoding="utf-8") as file:
        new_text = ""
        while True:
            line = file.readline()
            new_text += line
            if search_string in line:
                new_text += new_string
            if not line:
                break
    with open(filename, "w", encoding="utf-8") as file:
        file.write(new_text)
