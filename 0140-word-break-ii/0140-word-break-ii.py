class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        arr = []

        def dfs(x):
            if len(x) == 0:
                ans.append(" ".join(arr))
            for i in range(len(x)):
                if x[:i+1] in wordDict:
                    arr.append(x[:i+1])
                    dfs(x[i+1:])
                    arr.pop()
        
        dfs(s)
        return ans