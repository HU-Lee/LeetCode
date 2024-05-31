class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                del dic[num]
            else:
                dic[num] = 1
        return dic.keys()