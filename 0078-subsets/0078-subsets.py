class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        else:
            prev = self.subsets(nums[1:])
            return prev + list(map(lambda x: [nums[0]] + x, prev))