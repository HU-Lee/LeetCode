class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(arr: List[int]):
            if sorted(arr) != [1,2,3,4,5,6,7,8,9]:
                return False
            for x,y,z in [
                (1,2,3), (4,5,6), (7,8,9),
                (1,4,7), (2,5,8), (3,6,9),
                (1,5,9), (3,5,7)
            ]:
                if arr[x-1] + arr[y-1] + arr[z-1] != 15:
                    return False
            return True
        
        row = len(grid)
        col = len(grid[0])
        if row < 3 or col < 3:
            return 0

        cnt = 0
        for i in range(row-2):
            for j in range(col-2):
                if is_magic(grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3]):
                    cnt += 1
        
        return cnt