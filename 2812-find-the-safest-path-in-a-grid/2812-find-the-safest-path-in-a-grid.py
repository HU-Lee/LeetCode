class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        
        safes = [[-1]*n for _ in range(n)]
        q = []

        # safe calculate
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    safes[i][j] = 0
                    q.append((0,i,j))
        
        while q:
            dis, i, j = q.pop(0)
            for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < n and safes[ni][nj] == -1:
                    safes[ni][nj] = dis + 1
                    q.append((dis+1,ni,nj))
        
        # route search
        heap = [(-safes[0][0], 0, 0)]
        visited = [[False]*n for _ in range(n)]
        visited[0][0] = True
        while heap:
            x, i, j = heapq.heappop(heap)
            dis = -x
            if i == n-1 and j == n-1:
                return dis
            
            for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                    safe = min(dis, safes[ni][nj])
                    heapq.heappush(heap, (-safe, ni, nj))
                    visited[ni][nj] = True

        return -1
