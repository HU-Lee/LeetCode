class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h = len(board)
        w = len(board[0])

        visited = [[False for _ in range(w)] for _ in range(h)]

        def dfs(x,y,i):
            if i == len(word): return True
            elif x<0 or x>=h or y<0 or y>=w \
                 or word[i] != board[x][y] or visited[x][y]:
                 return False
            else:
                visited[x][y] = True
                res = dfs(x-1, y, i+1) \
                    or dfs(x+1, y, i+1) \
                    or dfs(x, y-1, i+1) \
                    or dfs(x, y+1, i+1)
                visited[x][y] = False
                return res

        for i in range(h):
            for j in range(w):
                if dfs(i,j,0):
                    return True
        return False
        
        