class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        dp = [[0]*(n+1) for _ in range(n)]
        
        # Sum of piles[i:]
        suffixs = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suffixs[i] = suffixs[i+1] + piles[i]
        
        for i in range(n-1, -1, -1):
            for m in range(1, n+1):
                if i + m*2 >= n:
                    dp[i][m] = suffixs[i]
                else:
                    # Assume that Bob does optimal
                    for j in range(1, 2 * m + 1):
                        dp[i][m] = max(dp[i][m], suffixs[i] - dp[i + j][max(m, j)])
        
        return dp[0][1]
