class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        temp = -101
        for num in nums:
            if num > temp:
                temp = num
                nums[cnt] = temp
                cnt += 1 
        return cnt