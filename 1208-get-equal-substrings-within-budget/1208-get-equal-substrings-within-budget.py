class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = len(s)
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(l)]

        ans = 0

        left = 0
        totalCosts = 0
        totalLength = 0
        for right in range(l):
            totalCosts += costs[right]
            totalLength += 1
            while left <= right and totalCosts > maxCost:
                totalCosts -= costs[left]
                totalLength -= 1
                left += 1
            ans = max(ans, totalLength)

        return ans