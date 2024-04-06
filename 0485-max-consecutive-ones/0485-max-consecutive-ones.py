class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for i in nums:
            if i == 1:
                cnt += 1
                if cnt > ans:
                    ans = cnt
            else:
                cnt = 0
        return ans