from string import printable
import random


class Node:
    def __init__(self, data=None):
        self.data: object = data
        self.next: Node = None


class linked_list:
    def __init__(self):
        self.head: Node = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head
            new_node.next = current
            self.head = new_node

    def print_linked_list(self):
        if self.head == None:
            print('None')
            return

        current = self.head
        while current:
            print(f'{current.data}->', end='')
            current = current.next
        print('end')

    def insert(self, item, index):
        new_node = Node(item)
        current = self.head

        for _ in range(index):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def indexof(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next

        return current.data

    def find(self, value):
        idx = 0
        current = self.head

        while(current.data != value):
            current = current.next
            idx += 1

        return idx

    def __len__(self):
        length = 0
        temp = self.head

        while temp:
            length += 1
            temp = temp.next

        return length


def get_random_string():
    length = random.randint(1, 8)
    return ''.join(random.sample(printable[:62], length))


lst = linked_list()
for i in range(random.randint(1, 50)):
    lst.append((i * 5))

lst.prepend('start')


lst.insert('end?', 2)
lst.print_linked_list()
print(len(lst), lst.indexof(5), lst.find(15))
