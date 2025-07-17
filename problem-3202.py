from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        max_len = 0

        for val in range(k):
            dp = [0] * k  
            for num in nums:
                r = num % k
                prev_r = (k + val - r) % k
                dp[r] = max(dp[r], dp[prev_r] + 1)
            max_len = max(max_len, max(dp))
        
        return max_len
