class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(x: int):
            return tuple(sorted(str(x)))  # sorted string tuple is a good "signature"
        
        target = count_digits(n)
        
        for i in range(31):  # 2^0 to 2^30 fits in 10^9
            if count_digits(1 << i) == target:
                return True
        return False
