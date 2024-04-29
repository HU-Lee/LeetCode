class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curr = 0
        for num in nums:
            curr = curr ^ num

        cnt = 0
        while curr > 0 or k > 0:
            if(curr%2 != k%2):
                cnt += 1
            curr = curr//2
            k = k//2

        return cnt