#!/usr/bin/python3

"""Program to Write a class Node that defines a node of a singly linked list"""


class Node:
    """Creates a class Node"""
    def __init__(self, data, next_node=None):
        """Constructor method __init__"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Setter method for data"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Setter method for next_node"""
        if Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""Program that defines a singly linked list"""


class SinglyLinkedList:
    """Creates a class SinglyLinkedList"""
    def __init__(self):
        """Constructor method __init__"""
        self.__head = None

    def __str__(self):
        """print method for printing the sll"""
        h = self.__head
        node = ""
        while (h):
            node += str(h.data)
            h = h.next_node
            if (h):
                node += "\n"
        return (node)

    def sorted_insert(self, value):
        """Method for insert a Node in sorted order"""
        h = self.__head
        while (h):
            if h.data > value:
                break
            tmp = h
            h = h.next_node
        new = Node(value, h)
        if h == self.__head:
            self.__head = new
        else:
            tmp.next_node = new
