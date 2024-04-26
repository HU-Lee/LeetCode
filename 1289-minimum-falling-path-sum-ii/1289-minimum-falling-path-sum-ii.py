class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if n == 1:
            return grid[0][0]

        arr = [0]*n

        for i in range(n):
            for j in range(n):
                grid[i][j] = min(arr[:j] + arr[j+1:]) + grid[i][j]
            arr = grid[i]
        
        return min(arr)