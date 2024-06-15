class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        stocks = sorted((capital[i], profits[i]) for i in range(n))
        used = [False] * n

        curr = w
        mx = []
        i = 0
        for _ in range(k):
            while i < n:
                if stocks[i][0] > curr:
                    break
                heapq.heappush(mx, -stocks[i][1])
                i += 1
            
            if not mx:
                break
            curr += (-heapq.heappop(mx))
            
        return curr
