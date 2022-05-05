from math import log2


class vector:
    def __init__(self, capacity=4):
        self.arr = [None for _ in range(capacity)]
        self.size = 0
        self.capacity = capacity

    def _resize(self, new_capacity):
        self.capacity = new_capacity

        temp_arr = [None for _ in range(self.capacity)]
        temp_arr[:self.size] = self.arr[:self.size]

        self.arr = temp_arr
        temp_arr = None

    def is_empty(self):
        return self.size == 0

    def at(self, index):
        return self.arr[index]

    def set(self, index, item):
        if self.arr[index] is None:
            self.size += 1
        self.arr[index] = item

    def push(self, item):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        self.arr[self.size] = item
        self.size += 1

    def insert(self, index, item):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i - 1]

        self.arr[index] = item
        self.size += 1

    def prepend(self, item):
        self.insert(0, item)

    def pop(self):
        self.size -= 1
        if self.size * 4 <= self.capacity:
            self._resize(self.capacity // 2)

        temp = self.arr[self.size]
        self.arr[self.size] = None

        return temp

    def delete(self, index):
        self.size -= 1
        for i in range(index, self.size):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.size] = None

    def remove(self, item):
        idx = 0
        while self.arr[idx] != None:
            if self.arr[idx] == item:
                self.delete(idx)

            else:
                idx += 1

    def find(self, item):
        for i in range(self.arr):
            if self.arr[i] == item:
                return i

        return -1

    def set_list(self, lst):
        if not self.is_empty():
            return

        self.size = len(lst)
        if self.size > self.capacity:
            self._resize(2**int(1 + log2(self.size)))
        self.arr = lst


x = vector(16)
x.set_list([1, 2, 3, 4] * 4)
x.remove(1)
print(x.arr, x.size, x.capacity, sep=', ')
