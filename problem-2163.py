from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)
        left_sum = sum(nums[:n])
        left_prefix = [0] * (n + 1)
        left_prefix[0] = left_sum
        
        for i in range(n, 2 * n):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i] + heapq.heappop(max_heap)
            left_prefix[i - n + 1] = left_sum

        min_heap = nums[2 * n:]
        heapq.heapify(min_heap)
        right_sum = sum(min_heap)
        right_suffix = [0] * (n + 1)
        right_suffix[n] = right_sum

        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i] - heapq.heappop(min_heap)
            right_suffix[i - n] = right_sum

        return min(left_prefix[i] - right_suffix[i] for i in range(n + 1))
