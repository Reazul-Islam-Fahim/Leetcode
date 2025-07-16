from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        max_len = 0

        for start in [0, 1]:
            length = 0
            expected = start
            for num in nums:
                if num % 2 == expected:
                    length += 1
                    expected ^= 1
            max_len = max(max_len, length)

        count_even = sum(1 for num in nums if num % 2 == 0)
        count_odd = len(nums) - count_even
        max_len = max(max_len, count_even, count_odd)

        return max_len
