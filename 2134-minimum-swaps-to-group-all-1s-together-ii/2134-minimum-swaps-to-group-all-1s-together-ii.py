class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)

        cur = sum(nums[:ones])
        mx = cur
        for i in range(n):
            idx = (i + ones) % n
            cur = cur - nums[i] + nums[idx]
            mx = max(mx, cur)
        
        return ones - mx