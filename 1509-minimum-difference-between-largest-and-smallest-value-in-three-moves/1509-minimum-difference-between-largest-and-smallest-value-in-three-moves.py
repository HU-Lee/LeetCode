class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        left, right = 0, n-4
        return min(nums[right+i] - nums[left+i] for i in range(4))