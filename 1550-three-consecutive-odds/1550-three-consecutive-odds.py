class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        stack = 0
        for i in arr:
            if i % 2 == 1:
                stack += 1
            else:
                stack = 0
            if stack >= 3:
                return True
        return False