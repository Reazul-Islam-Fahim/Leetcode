from bisect import bisect_right
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        
        end_times = [event[1] for event in events]
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            s, e, v = events[i - 1]
            prev = bisect_right(end_times, s - 1)
            
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i - 1][j], dp[prev][j - 1] + v)
        
        return dp[n][k]
