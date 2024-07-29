class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        for idx, r in enumerate(rating):
            left_small, right_big = 0,0
            for x in rating[:idx]:
                if x < r:
                    left_small += 1
            for y in rating[idx+1:]:
                if y > r:
                    right_big += 1
            
            ans += left_small*right_big + (idx-left_small)*(n-1-idx-right_big)
        return ans