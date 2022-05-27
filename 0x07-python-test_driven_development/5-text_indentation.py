#!/usr/bin/python3

"""5-text_indentation module that prints a text with 2 new lines \
    after each of these characters: '.', '?'and ':'"""


def text_indentation(text):
    """Function that prints a text with 2 new lines \
        after each of these characters: '.', '?' and ':'"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text1 = text.replace("?", "?(split@)")
    text2 = text1.replace(":", ":(split@)")
    text3 = text2.replace(".", ".(split@)")
    text4 = text3.split("(split@)")
    for x in range(len(text4) - 1):
        print(f"{text4[x].strip()}\n\n", end="")
    if text4[-1] != "":
        print(f"{text4[-1].strip()}", end="")
