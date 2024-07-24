class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def changeNumber(num: int):
            ans = 0
            exp = 0
            if num == 0: return mapping[0]
            while num > 0:
                r = num % 10
                ans += mapping[r]*(10**exp)
                num = num // 10
                exp += 1
            return ans
        
        return sorted(nums, key=lambda x: changeNumber(x))