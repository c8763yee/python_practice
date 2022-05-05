from random import randint


class BigO:
    def __init__(self):
        self.array = [randint(1, 1000) for _ in range(1000)]
        self.len = 1000

    # def bubble_sort()
    def binary_search(self, value):
        low_index = 0
        high_index = self.len - 1
        array = sorted(self.array)
        print(array)
        while low_index <= high_index:
            mid_index = (high_index + low_index) // 2
            if array[mid_index] < value:
                low_index = mid_index + 1

            elif array[mid_index] > value:
                high_index = mid_index + 1

            else:
                print(f'found {value} in array[{mid_index}]')
                low_index = high_index + 1


BigO().binary_search(1)
