import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.nums.append(val)
        self.index_map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        idx = self.index_map[val]
        last_val = self.nums[-1]
        self.nums[idx] = last_val
        self.index_map[last_val] = idx
        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
