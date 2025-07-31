class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()

        for num in arr:
            cur = {num | x for x in cur}
            cur.add(num)
            res |= cur

        return len(res)
