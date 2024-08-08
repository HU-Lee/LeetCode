class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        direction = [(0,1), (1,0), (0,-1), (-1,0)]

        cnt = 0
        ans = []
        x,y = rStart, cStart
        step = 1
        cur = 0
        while cnt < rows*cols:
            for _ in range(step):
                if 0<=x<rows and 0<=y<cols:
                    cnt += 1
                    ans.append((x,y))
                x,y = x + direction[cur][0], y + direction[cur][1]
            # Set next
            cur = (cur+1)%4
            if cur % 2 == 0:
                step += 1
            print(x,y,cnt)

        return ans