class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        letters += letters.upper()
        arr = [0]*52
        for l in s:
            arr[letters.index(l)] += 1

        print(arr)
        
        cnt = 0
        odd = False
        for n in arr:
            if n % 2 == 0:
                cnt += n
            else:
                cnt += n-1
                odd = True
        
        if odd:
            cnt += 1
        return cnt