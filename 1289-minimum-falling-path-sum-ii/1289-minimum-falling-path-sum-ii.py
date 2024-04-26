class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if n == 1:
            return grid[0][0]

        arr = [
            [0]*n for _ in range(n+1)
        ]

        for i in range(1,n+1):
            for j in range(n):
                arr[i][j] = min(arr[i-1][:j] + arr[i-1][j+1:]) + grid[i-1][j]
        
        return min(arr[n])