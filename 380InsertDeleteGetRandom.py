#https://leetcode.com/problems/insert-delete-getrandom-o1

import random

class RandomizedSet:

    def __init__(self):
        self.set = {}

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set[val] = 1
            return True
        
    def remove(self, val: int) -> bool:
        result = self.set.pop(val, False)
        return result

    def getRandom(self) -> int:
        return random.choice(list(self.set.keys()))


obj = RandomizedSet()
print(obj.insert(1))
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())