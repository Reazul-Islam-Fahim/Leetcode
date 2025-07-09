class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        i = 0
        result = 1  

        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            length = j - i
            if length > 1:
                result += (length - 1)
            i = j

        return result
