class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        for idx, g in enumerate(grid):
            if g[0] == 0:
                grid[idx] = list(map(lambda x: 1-x, grid[idx]))
        for idx2 in range(w):
            cur = sum(grid[i][idx2] for i in range(h))
            if cur <= h // 2:
                for i in range(h):
                    grid[i][idx2] = 1 - grid[i][idx2]
        
        ans = 0
        for g in grid:
            ans += sum(2**(w-1-x)*g[x] for x in range(w))
        return ans
