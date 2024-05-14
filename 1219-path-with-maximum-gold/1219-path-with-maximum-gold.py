class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def isValid(i,j):
            return 0<=i<m and 0<=j<n \
                and (i,j) not in path and grid[i][j] > 0
        
        def dfs(i,j):
            if not isValid(i,j): return 0
            val_store = grid[i][j]
            grid[i][j] = 0
            result = 0
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                result = max(result, dfs(i+di, j+dj))
            grid[i][j] = val_store
            return val_store + result

        ans = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] > 0:
                    ans = max(ans, dfs(x,y))
        
        return ans
