class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Improved by reference
        n = len(grid)

        if n == 1:
            return grid[0][0]

        arr = [0]*n

        for i in range(n):
            min1 = arr.index(min(arr))
            min2 = arr.index(min(arr[:min1] + arr[min1+1:]))
            for j in range(n):
                grid[i][j] += (arr[min1] if min1 != j else arr[min2])
            arr = grid[i]
        
        return min(arr)