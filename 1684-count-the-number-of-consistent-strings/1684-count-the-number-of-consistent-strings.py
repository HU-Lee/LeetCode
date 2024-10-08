class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            count += 1
            for l in word:
                if l not in allowed:
                    count -= 1
                    break
        return count