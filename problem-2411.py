from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        bit_index = [-1] * 32
        res = [0] * n

        for i in range(n - 1, -1, -1):
            for b in range(32):
                if nums[i] & (1 << b):
                    bit_index[b] = i
            max_reach = max([idx for idx in bit_index if idx != -1], default=i)
            res[i] = max_reach - i + 1
        return res
