from collections import Counter
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val

        self.counter2[old_val] -= 1
        if self.counter2[old_val] == 0:
            del self.counter2[old_val]

        self.nums2[index] = new_val
        self.counter2[new_val] += 1

    def count(self, tot: int) -> int:
        result = 0
        for num in self.nums1:
            target = tot - num
            result += self.counter2.get(target, 0)
        return result
