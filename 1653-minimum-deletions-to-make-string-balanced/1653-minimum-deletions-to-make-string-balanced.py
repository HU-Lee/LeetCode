class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt = 0
        ans = 0
        for l in s:
            if l == 'b':
                cnt += 1 
            elif cnt > 0:
                # a next to b: delete this a, or delete all b
                ans = min(ans+1, cnt)
        return ans