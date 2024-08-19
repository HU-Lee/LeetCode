class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        ans = 0
        cur = n
        for i in range(3, n+1):
            if i > cur: break
            while cur % i == 0:
                ans += i
                cur = cur // i
        if cur % 2 == 0:
            ans += 2
            cur = cur // 2
        return ans

