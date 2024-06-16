class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        idx, ans = 0,0
        missing = 1

        while missing <= n:
            if idx < len(nums) and missing >= nums[idx]:
                missing += nums[idx]
                idx += 1
            else:
                missing += missing
                ans += 1
                
        return ans