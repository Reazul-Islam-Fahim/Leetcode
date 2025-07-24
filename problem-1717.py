class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s: str, first: str, second: str, points: int) -> (str, int):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(ch)
            return ''.join(stack), score
        
        total_score = 0
        
        if x >= y:
            s, score1 = remove_pair(s, 'a', 'b', x)
            s, score2 = remove_pair(s, 'b', 'a', y)
        else:
            s, score1 = remove_pair(s, 'b', 'a', y)
            s, score2 = remove_pair(s, 'a', 'b', x)
        
        return score1 + score2
