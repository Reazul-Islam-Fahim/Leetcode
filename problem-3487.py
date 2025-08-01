from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)

        seen = set()
        for num in nums:
            if num >= 0:
                seen.add(num)
        
        return sum(seen)
