from string import printable
import random


class Node:
    def __init__(self, data=None):
        self.data: object = data
        self.prev: Node = None
        self.next: Node = None


class linked_list:
    def __init__(self):
        self.length = 0
        self.head: Node = None
        self.tail = None
        #self.sentinel = Node()

    def check_vaild_index(self, idx):
        idx = idx if idx >= 0 else ~idx
        return -1 if idx >= self.length else idx

    def remove_tail(self):
        if self.length < 2:
            raise Exception('linked list is empty')

        self.length -= 1
        self.tail.prev.next = None
        self.tail = self.tail.prev

    def pop_front(self):
        value = self.head.data
        self.head = self.head.next
        self.length -= 1
        return value

    def erase(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next

        current.data = current.next.data
        current.next = current.next.next
        self.length -= 1

    def push_back(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node

        else:
            # with tail
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

            # without tail
            """ current = self.head
            for _ in range(self.length - 1):
                current = current.next

            current.next = new_node """

        self.length += 1

    def push_front(self, data):
        self.length += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, item, index):
        index = self.check_vaild_index(index)

        new_node = Node(item)
        current = self.head

        for _ in range(index):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def print_linked_list(self):
        if self.head == None:
            print('None')
            return

        current = self.head
        for _ in range(self.length):
            print(f'{current.data}->', end='')
            current = current.next
        print('end')

    def value_at(self, idx):
        current = self.head
        for _ in range(idx if idx >= 0 else ~idx):
            current = current.next

        return current.data

    def find(self, value):
        idx = 0
        current = self.head

        while(current.next):
            if current.data == value:
                return idx
            current = current.next
            idx += 1

        return -1

    def size(self):
        return self.length

    # find by index using recursive(not working)
    """  def find_by_index_using_recursive(self, index):
    if index < 0 and ~index < length:  # make sure index is not out of range and index is positive
        index = ~index

    if index >= self.length:
        return None

    if index == 0:
        return self.head.data

    return self.find_by_index_using_recursive(index - 1) """

    def __len__(self):
        return self.length


def get_random_string():
    length = random.randint(1, 8)
    return ''.join(random.sample(printable[:62], length))


lst = linked_list()
lst.push_back('gogo')
for i in range(10):
    lst.push_back((i, chr(0x41 + i)))

lst.push_front('start')
lst.insert('end?', 0)
lst.erase(1)
lst.push_back(7414)


print(lst.pop_front())
lst.print_linked_list()
