class Solution:
    mod = 10**9 + 7

    def checkRecord(self, n: int) -> int:
        dps = [
            [1,1,0], # 0 absent with n consecutive late
            [1,0,0], # 1 absent with n consecutive late
        ]
        if n == 1:
            return 3
        else:
            for i in range(2, n+1):
                nxt = [[0,0,0],[0,0,0]]
                nxt[0][0] = sum(dps[0]) % self.mod
                nxt[0][1] = dps[0][0]
                nxt[0][2] = dps[0][1]
                nxt[1][0] = (sum(dps[1]) + sum(dps[0])) % self.mod
                nxt[1][1] = dps[1][0]
                nxt[1][2] = dps[1][1]
                dps = nxt
            return sum(dps[0]+dps[1]) % self.mod
