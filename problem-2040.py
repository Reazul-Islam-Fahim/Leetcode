from bisect import bisect_right, bisect_left
from typing import List
import math

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_less_equal(x):
            count = 0
            for a in nums1:
                if a > 0:
                    count += bisect_right(nums2, x // a)
                elif a < 0:
                    count += len(nums2) - bisect_left(nums2, math.ceil(x / a))
                else:
                    if x >= 0:
                        count += len(nums2)
            return count

        nums1.sort()
        nums2.sort()

        min_prod = min(nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1])
        max_prod = max(nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1])

        low, high = min_prod, max_prod
        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
