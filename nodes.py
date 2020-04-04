"""
Module with different nodes shaped to different data structures
"""


class LinkedListNode:
    def __init__(self, value):
        self.next_node = None
        self.data = value


class OpenAddressingNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None

    def __eq__(self, other):
        return self.key == other

    def __repr__(self):
        return f'{self.key}: {self.value}'


class StaticLinkingNode:
    def __init__(self, key, value, node_counter):
        self.key = key
        self.value = value
        self.next = None
        self.counter = node_counter

    def __repr__(self):
        return f'{self.counter}_Node'
