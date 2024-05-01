class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0
        for idx, w in enumerate(word):
            if w == ch:
                i = idx
                break
        return word[:i+1][::-1] + word[i+1:]