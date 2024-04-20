class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def is_land(x:int,y:int):
            return 0<=x<len(land) and 0<=y<len(land[0]) and land[x][y] == 1

        ans = []
        path = []

        def dfs(x:int,y:int):
            if is_land(x+1,y) and is_land(x,y+1):
                dfs(x+1,y+1)
            elif is_land(x+1,y):
                dfs(x+1,y)
            elif is_land(x,y+1):
                dfs(x,y+1)
            else:
                path.extend([x,y])
                for w in range(path[0], path[2]+1):
                    for h in range(path[1], path[3]+1):
                        land[w][h] = 0
                ans.append(path)

        for i in range(len(land)):
            for j in range(len(land[0])):
                if is_land(i,j):
                    path = [i,j]
                    dfs(i,j)
        return ans 