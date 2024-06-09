class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(list)
        dic[0].append(-1)

        tmp = 0
        for idx, num in enumerate(nums):
            tmp = (tmp + num) % k
            dic[tmp].append(idx)
        
        ans = 0
        for key in dic:
            l = len(dic[key])
            ans += l*(l-1)//2
        return ans