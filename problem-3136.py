class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set("aeiouAEIOU")
        has_vowel = has_consonant = False

        for c in word:
            if not c.isalnum():
                return False
            if c in vowels:
                has_vowel = True
            elif c.isalpha():
                has_consonant = True

        return has_vowel and has_consonant
