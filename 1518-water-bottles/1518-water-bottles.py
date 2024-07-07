class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        full = numBottles
        rest = 0
        while full > 0:
            ans += full
            full,rest = (full + rest) // numExchange, (full + rest) % numExchange
        return ans