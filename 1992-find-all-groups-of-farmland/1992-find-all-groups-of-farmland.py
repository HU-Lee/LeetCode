class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def is_land(x:int,y:int):
            return 0<=x<len(land) and 0<=y<len(land[0]) and land[x][y] == 1

        ans = []
        path = []

        def dfs(x:int,y:int):
            print(path)
            if is_land(x+1,y) and is_land(x,y+1):
                dfs(x+1,y+1)
            elif is_land(x+1,y):
                dfs(x+1,y)
            elif is_land(x,y+1):
                dfs(x,y+1)
            else:
                val = path + [x,y]
                for w in range(val[0], val[2]+1):
                    for h in range(val[1], val[3]+1):
                        land[w][h] = 0
                ans.append(val)

        for i in range(len(land)):
            for j in range(len(land[0])):
                if is_land(i,j):
                    path = [i,j]
                    dfs(i,j)
                    path = []
        return ans 