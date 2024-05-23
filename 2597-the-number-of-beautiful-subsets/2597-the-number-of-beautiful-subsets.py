class Solution:
    ans = 0

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        l = len(nums)
        cnts = [0 for _ in range(-k, nums[-1]+1)]


        def dfs(x):
            if x >= l:
                self.ans += 1
                return
            else:
                if cnts[nums[x]-k] == 0:
                    cnts[nums[x]] += 1
                    dfs(x+1)
                    cnts[nums[x]] -= 1
                dfs(x+1)
        
        dfs(0)
        
        # Delete empty dfs(l)
        return self.ans - 1
