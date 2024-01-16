# url: https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=daily-question&envId=2024-01-16

import random


class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        index = self.val_to_index[val]
        last_value = self.values[-1]
        self.values[index] = last_value
        self.val_to_index[last_value] = index
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
