from nodes import LinkedListNode as Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def add_at(self, value, index):
        new_node = Node(value)
        previous_node = None
        current_node = self.head
        current_index = 0
        while current_index < index and current_node.next_node:
            previous_node = current_node
            current_node = current_node.next_node
            current_index += 1
        if current_index == index:
            previous_node.next_node = new_node
            current_node.next_node = current_node
            return True
        else:
            # List not long enough
            return False

    def remove(self, index):
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.data == index:
                if previous_node:
                    previous_node.next_node = current_node.next_node
                else:
                    self.head = current_node.next_node
                self.size -= 1
                return True
            previous_node = current_node
            current_node = current_node.next_node
        return False

    def find(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next_node
        return False

    def __iter__(self):
        pointer_node = self.head
        while pointer_node.next_node:
            yield pointer_node.data
            pointer_node = pointer_node.next_node
        else:
            yield pointer_node.data
        return None

    def __str__(self):
        return f'[{", ".join((str(elem) for elem in self.__iter__()))}]'


if __name__ == '__main__':
    linked_list = LinkedList()
    for new_elem in range(1, 10):
        linked_list.add(new_elem)

    for elem in linked_list:
        print(elem)
