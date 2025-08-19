class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans, numSubarray = 0, 0
        for num in nums:
            if num == 0:
                numSubarray += 1
            else:
                numSubarray = 0
            ans += numSubarray
        return ans
