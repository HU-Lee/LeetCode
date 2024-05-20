class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        mul = 0
        for num in nums:
            mul = mul | num
        
        return mul * (2**(len(nums)-1))