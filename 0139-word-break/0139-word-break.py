class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        def dfs(x):
            if len(x) == 0:
                return True
            if x in dic:
                return dic[x]
            for i in range(len(x)):
                if x[:i+1] in wordDict and dfs(x[i+1:]):
                    dic[x] = True
                    return True
            dic[x] = False
            return False
        
        return dfs(s)