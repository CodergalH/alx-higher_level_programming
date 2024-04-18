#!/usr/bin/python3
"""
Author: Glorious Oyovwuvwe Ohwojeheri <gloriousohwojeheri608@gmail.com>
Purpose: Define a singly linked lista and its node class
"""


class Node:
    """
    A class representing/defining a node in the linked list.
    Private instance attribute: data:
        property def data(self): to retrieve it
        property setter def data(self, value): to set it:
            data must be an integer, otherwise raise a TypeError exception 
            with the message data must be an integer

    Private instance attribute: next_node:
        property def next_node(self): to retrieve it
        property setter def next_node(self, value): to set it:
            next_node can be None or must be a Node, otherwise raise a 
            TypeError exception with the message next_node must be a Node object

    Instantiation with data and next_node:
        def __init__(self, data, next_node=None):
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """
        Private instance attribute: head (no setter or getter)
        Simple instantiation: def __init__(self):
        Should be printable:
            print the entire list in stdout
            one node number by line
        Public instance method: def sorted_insert(self, value): that inserts 
        a new Node into the correct sorted position in the list 
        (increasing order)
    """


    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        Adds a new node at the correct position to keep the list sorted.
        If the linked list is empty, adds it as the first element.
        Otherwise, iterates through the elements until finds the right place  
        to insert the new value.
        
        :param value: The integer that will be added to the list.
        :type value: int
        """


        new_node = Node(value)
        prev = self.__head
        if prev is None or prev.data <= value:
            new_node.next_node = prev
            prev = new_node
        
        while prev and prev.next_node and prev.next_node.data < value:
            prev = prev.next_node

        new_node.next_node = prev.next_node
        prev.next_node = new_node

    def __str__(self):
        current = self.__head
        while current:
            if current.next_node is None:
                print(current.data, end="")
            else:
                print(current.data)
            current = current.next_node
        return ''
