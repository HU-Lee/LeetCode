class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = len(s)
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(l)]
        print(costs)

        dps = [(0,0)]*l # values that last index is i
        dps[0] = (0,0) if costs[0] > maxCost else (1,costs[0])
        for i in range(1, l):
            prev_length, prev_cost = dps[i-1]
            if prev_cost + costs[i] <= maxCost:
                dps[i] = (prev_length + 1, prev_cost + costs[i])
            elif costs[i] <= maxCost:
                dps[i] = (1, costs[i])
        
        return max(x[0] for x in dps)
