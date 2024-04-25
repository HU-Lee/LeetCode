class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        arr = [0]*26
        for x in s:
            i = ord(x)-ord('a')
            mi = max(0,i-k)
            mx = min(25,i+k)
            arr[i] = max(arr[mi:mx+1]) + 1
        return max(arr)
