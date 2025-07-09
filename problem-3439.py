from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []

        gaps.append(startTime[0] - 0)

        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])

        gaps.append(eventTime - endTime[-1])

        window_size = k + 1
        max_sum = 0
        current_sum = sum(gaps[:window_size])

        max_sum = current_sum

        for i in range(window_size, len(gaps)):
            current_sum += gaps[i] - gaps[i - window_size]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
