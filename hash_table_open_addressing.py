from uuid import uuid4
from pprint import pp
from random import randint
from nodes import OpenAddressingNode as Node


class HashTable:
    """
    HashTable with open addressing collision solving
    based on linear probing with odd step to cover all values in even amount of buckets
    """

    INITIAL_CAPACITY = 8  # should be even
    RESIZE_PERCENTAGE = 65

    def __init__(self):
        self.load = 0
        self.buckets = [None] * self.INITIAL_CAPACITY
        self.current_size = len(self.buckets)
        self.step = lambda x: (x + 3) % self.current_size

        # inner linked_list part
        self.head = None
        self.tail = None

    def __getitem__(self, item):
        return self._find(item)

    def __setitem__(self, _key, _value):
        return self._insert(_key, _value)

    def _hash(self, _key: str) -> int:
        hash_sum = 0
        for index, char in enumerate(_key):
            hash_sum += index + len(_key) + id(char)

        hash_sum %= len(self.buckets)
        return hash_sum

    def _get_linked_node(self, key, value) -> Node:
        """
        Link new node with last present node, or create a new one
        """
        new_node = Node(key, value)
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        return new_node

    def _is_key_hashable(self, key):
        hash_dunder = getattr(key, "__hash__")
        if not callable(hash_dunder):
            raise TypeError(f'unhashable type: {type(key).__name__}')

    def _insert(self, _key, _value) -> bool:
        self._is_key_hashable(_key)
        self._resize()
        self.load += 1
        new_node = self._get_linked_node(_key, _value)
        index = self._hash(_key)
        if not self.buckets[index]:
            self.buckets[index] = new_node
            return True
        else:  # probing
            new_index = self.step(index)
            while True:
                if not self.buckets[new_index]:
                    self.buckets[new_index] = new_node
                    return True
                new_index = self.step(new_index)

    def _find(self, _key):
        index = self._hash(_key)
        if _key == self.buckets[index]:
            return self.buckets[index].value
        else:
            new_index = self.step(index)
            while index != new_index:  # when we run dict for 2 times we raise KeyError
                if _key == self.buckets[new_index]:
                    return self.buckets[new_index].value
                new_index = self.step(new_index)
            else:
                raise KeyError

    def _resize(self) -> None:
        percentage = self.load / self.current_size * 100
        if percentage > self.RESIZE_PERCENTAGE:
            self.buckets += [None] * self.current_size
            self.current_size = len(self.buckets)

    def __iter__(self):
        pointer_node = self.head
        while pointer_node.next_node:
            yield (pointer_node.key, pointer_node.value)
            pointer_node = pointer_node.next_node
        else:
            yield (pointer_node.key, pointer_node.value)
        return None

    @classmethod
    def populate(cls, *, insertions_number):
        instance = cls()
        for _ in range(insertions_number):
            instance[uuid4().hex[-randint(3, 9):]] = uuid4().hex[-4:]
        return instance


if __name__ == '__main__':
    ht = HashTable()
    filler_string = 'abcdefghijklmnopqrstuvwxyzasdfasdfgfgdsdgsdgsdsffdsafsgdsdgdfdfdsdgsdgsdgssgdgddafsdasfasdsfdaasdf'
    for counter, letter in enumerate(filler_string):
        ht[letter] = counter
    for letter in filler_string:
        print(ht[letter])
    for key, value in ht:
        print(key, value)
    print(ht.buckets)
