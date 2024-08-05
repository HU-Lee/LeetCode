class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        q = []
        for i in range(n):
            tmp = 0
            for j in range(i, n):
                tmp += nums[j]
                heapq.heappush(q, tmp)
        
        ans = 0
        for k in range(1, right+1):
            x = heapq.heappop(q)
            if k < left:
                continue
            else:
                ans = (ans + x) % 1000000007
        
        return ans