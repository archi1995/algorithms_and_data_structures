from uuid import uuid4
from random import randint
from nodes import StaticLinkingNode as Node


class HashTable:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.size = 0
        self.buckets = [None] * self.INITIAL_CAPACITY

    @classmethod
    def populate(cls, *, nodes_number):
        instance = cls()
        for _ in range(nodes_number):
            instance.insert(uuid4().hex[-randint(3, 9):], uuid4().hex[-4:])
        return instance

    @classmethod
    def hash(cls, key: str) -> int:
        hash_sum = 0
        for index, char in enumerate(key):
            hash_sum += index + len(key) + id(char)
            hash_sum %= cls.INITIAL_CAPACITY
        return hash_sum

    def _is_key_hashable(self, key):
        hash_dunder = getattr(key, "__hash__")
        if not callable(hash_dunder):
            raise TypeError(f'unhashable type: {type(key).__name__}')

    def insert(self, key, value):
        self._is_key_hashable(key)
        self.size += 1
        index = self.hash(key)
        if not (node := self.buckets[index]):
            self.buckets[index] = Node(key, value, 1)
            return None
        prev = node
        node_counter = 1
        while node:
            node_counter += 1
            prev = node
            node = node.next
        prev.next = Node(key, value, node_counter)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node and node.key != key:
            node = node.next
        if node:
            return node.value
        else:
            return None

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = node
        while node and node.key != key:
            prev = node
            node = node.next
        if node:
            self.size -= 1
            result = node.value
            if prev:
                prev.next = prev.next.next
            else:
                node = None
            return result
        else:
            return None


if __name__ == '__main__':
    ht = HashTable.populate(nodes_number=30)
    ht.remove(ht.buckets[0].key)
    print(ht.buckets)
