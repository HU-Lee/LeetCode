class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        counts = [0] * 100001

        for num in nums:
            counts[num + 50000] += 1
        
        ans = []
        for idx, c in enumerate(counts):
            if c > 0:
                ans += [idx-50000] * c

        return ans