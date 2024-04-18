class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for g in grid:
            ans += 4*sum(g)
            for i in range(len(g)-1):
                if g[i] == 1 and g[i+1] == 1:
                    ans -= 2
        for i in range(len(grid)-1):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and grid[i+1][j] == 1:
                    ans -= 2
        return ans                
