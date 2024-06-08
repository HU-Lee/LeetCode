class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {
            0: -1
        }
        cnt = 0
        for idx, num in enumerate(nums):
            cnt = (cnt + num)%k
            if cnt in dic:
                if idx - dic[cnt] > 1:
                    return True
            else:
                dic[cnt] = idx
        return False