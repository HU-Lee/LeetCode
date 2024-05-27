class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        x = 0
        l = len(nums)
        idx = 0

        while idx < l:
            if nums[idx] < x:
                idx += 1
                continue
            if x == l-idx:
                return x
            else:
                x += 1
        
        return -1
