class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        dps = [0]*(n+1)
        dps[3] = 1 if (
            (rating[0] < rating[1] < rating[2]) or
            (rating[0] > rating[1] > rating[2])
        ) else 0

        for i in range(4, n+1):
            cnt = dps[i-1]
            for x in range(i-1):
                for y in range(x+1, i-1):
                    if rating[x] < rating[y] < rating[i-1] \
                    or rating[x] > rating[y] > rating[i-1]:
                        cnt += 1
            dps[i] = cnt
        
        print(dps)
        return dps[n]