class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        main_heap = []
        for i in range(len(quality)):
            w = wage[i]
            q = quality[i]
            heapq.heappush(main_heap, (w/q, i))
        q_heap = []
        ans = math.inf
        base_ratio = 0
        for n in range(len(quality)):
            base_ratio, i = heapq.heappop(main_heap)
            heapq.heappush(q_heap, -quality[i])
            if len(q_heap) > k:
                heapq.heappop(q_heap)
            if n >= k-1:
                ans = min(ans, -base_ratio*sum(q_heap))
        return ans