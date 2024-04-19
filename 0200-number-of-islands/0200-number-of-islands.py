class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def is_land(x:int,y:int):
            return 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == "1"

        def dfs(x:int,y:int):
            if is_land(x,y):
                grid[x][y] = "0"
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y+1)
                dfs(x,y-1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_land(i,j):
                    cnt += 1
                    dfs(i,j)
        return cnt 