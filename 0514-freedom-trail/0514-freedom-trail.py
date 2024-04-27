class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Get word info
        dic = defaultdict(list)
        for idx, x in enumerate(ring):
            dic[x].append(idx)

        arr = [
            [-1]*len(ring) for _ in range(len(key)+1)
        ]
        def dfs(i, curr):
            if arr[i][curr] > -1:
                pass
            elif i == len(key):
                arr[i][curr] = 0
            else:
                ans = math.inf
                c = key[i]
                for x in dic[c]:
                    a = abs(x-curr)
                    mi = min(a, len(ring)-a)
                    ans = min(ans, dfs(i+1,x) + mi)
                arr[i][curr] = ans
            return arr[i][curr]
        
        print(arr)
        return dfs(0,0) + len(key)