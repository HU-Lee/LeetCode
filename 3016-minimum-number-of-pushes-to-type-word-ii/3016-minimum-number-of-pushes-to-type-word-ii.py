class Solution:
    def minimumPushes(self, word: str) -> int:
        arr = [0]*26
        for w in word:
            x = ord(w) - ord('a')
            arr[x] += 1
        arr = sorted(arr, reverse=True)
        ans = 0
        for idx, val in enumerate(arr):
            ans += val*(idx // 8 + 1)
        return ans