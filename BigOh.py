from itertools import count
from random import randint


class BigO:
    def __init__(self, length):
        self.array = [randint(1, length) for _ in range(length)]
        self.len = length

    def binary_search(self, value):
        low_index = 0
        high_index = self.len - 1
        array = sorted(self.array)

        while low_index < high_index:
            mid_index = (1 + high_index + low_index) // 2

            if high_index - low_index == 1:
                break

            if array[mid_index] == value:
                print(f'found {value} in array[{mid_index}]')
                return

            if array[mid_index] < value:
                low_index = mid_index

            elif array[mid_index] > value:
                high_index = mid_index

        print(f'{value} not found in array')


BigO(1000).binary_search(randint(1, 1000))
