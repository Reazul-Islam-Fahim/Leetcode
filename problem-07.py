#takes 49ms 

# class Solution:
#     def reverse(self, x: int) -> int:
#         INT_MIN, INT_MAX = -2**31, 2**31 - 1
#         res = 0
#         sign = -1 if x < 0 else 1
#         x = abs(x)

#         while x != 0:
#             digit = x % 10
#             x //= 10

#             if res > (INT_MAX - digit) // 10:
#                 return 0

#             res = res * 10 + digit

#         return sign * res


#takes 37ms

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        reversed_str = str(abs(x))[::-1]
        res = sign * int(reversed_str)
        
        if res < INT_MIN or res > INT_MAX:
            return 0
        return res
