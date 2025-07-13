from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child = cookie = count = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                count += 1
                child += 1
            cookie += 1  
        
        return count
