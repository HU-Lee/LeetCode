class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        main_arr = sorted([(wage[i]/quality[i], quality[i]) for i in range(len(quality))])
        q_heap = []
        q_total = 0
        ans = math.inf
        for base_ratio, q in main_arr:
            q_total += q
            heapq.heappush(q_heap, -q)
            while len(q_heap) > k:
                q_total += heapq.heappop(q_heap)
            if len(q_heap) == k:
                ans = min(ans, base_ratio*q_total)
        return ans