class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        cnts = [0] * 100001
        for num in nums:
            cnts[num] += 1
        
        ans = 0
        tmp = 0
        for val, cnt in enumerate(cnts):
            if cnt > 1:
                ans -= val * (cnt-1)
                tmp += cnt-1
            elif cnt == 0 and tmp > 0:
                ans += val
                tmp -= 1
        if tmp > 0:
            ans += 100001*tmp + tmp*(tmp-1)//2
        return ans