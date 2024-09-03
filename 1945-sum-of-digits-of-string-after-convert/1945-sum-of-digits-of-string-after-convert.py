class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = 0
        for idx, val in enumerate(s):
            n += (100**idx)*(ord(val) - ord('a') + 1)
        
        for _ in range(k):
            new_n = 0
            while n > 0:
                new_n += n % 10
                n = n // 10
            n = new_n
        
        return n