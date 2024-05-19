class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # any 2 pair nodes can get XOR operation
        mx = sum(max(num, num ^k) for num in nums)
        changed = sum(1 for num in nums if num ^ k > num)
        if changed % 2 == 0:
            return mx
        else:
            return mx - min(abs(num - (num ^ k)) for num in nums)