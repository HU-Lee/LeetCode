class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_pel(x):
            return x == x[::-1]

        l = len(s)
        if l == 1: return [[s]] if is_pel(s) else []
        
        ans = []
        for i in range(1,l):
            if is_pel(s[:i]):
                for rec in self.partition(s[i:]):
                    ans.append([s[:i]] + rec)
        
        if is_pel(s):
            ans.append([s])

        return ans
