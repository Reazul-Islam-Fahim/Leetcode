from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        positions = [pos for pos, _ in fruits]
        amounts = [amount for _, amount in fruits]
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + amounts[i]

        def get_sum(left_idx: int, right_idx: int) -> int:
            return prefix[right_idx + 1] - prefix[left_idx]
        
        max_fruits = 0

        for direction in ['left', 'right']:
            i = 0
            for j in range(n):
                left = fruits[i][0]
                right = fruits[j][0]

                if direction == 'left':
                    cost = min(
                        abs(startPos - left) + abs(right - left),
                        abs(startPos - right) + abs(right - left)
                    )
                else:
                    cost = min(
                        abs(startPos - right) + abs(right - left),
                        abs(startPos - left) + abs(right - left)
                    )

                while i <= j and cost > k:
                    i += 1
                    if i <= j:
                        left = fruits[i][0]
                        cost = min(
                            abs(startPos - left) + abs(right - left),
                            abs(startPos - right) + abs(right - left)
                        )

                if i <= j:
                    max_fruits = max(max_fruits, get_sum(i, j))

        return max_fruits
