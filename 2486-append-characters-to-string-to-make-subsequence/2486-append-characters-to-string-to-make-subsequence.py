class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        combo = 0
        for i in range(len(s)):
            if combo == len(t):
                break
            if s[i] == t[combo]:
                combo += 1
        
        return len(t) - combo