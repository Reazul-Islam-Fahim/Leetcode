class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for d in "9876543210":
            s = d * 3
            if s in num:
                return s
        return ""
