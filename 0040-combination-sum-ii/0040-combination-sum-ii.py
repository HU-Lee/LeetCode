class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        n = len(candidates)
        
        ans = []
        comb = []
        def dfs(i):
            if sum(comb) == target:
                ans.append(comb.copy())
                return
            if i >= n or sum(comb) > target:
                return
            for j in range(i, n):
                # Remove duplicates
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                comb.append(candidates[j])
                dfs(j+1)
                comb.pop()
        
        dfs(0)
        return ans