#!/usr/bin/python3

"""Mylist class"""


class MyList(list):
    """Mylist class"""
    mylist = []

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        newlist = self[:]
        newlist.sort()
        print(newlist)
