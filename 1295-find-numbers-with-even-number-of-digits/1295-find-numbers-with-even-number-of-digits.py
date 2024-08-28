class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            while num >= 100:
                num = num // 100
            if 10 <= num:
                ans += 1
        return ans