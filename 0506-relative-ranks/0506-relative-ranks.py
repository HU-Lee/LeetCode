class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []

        for idx, s in enumerate(score):
            heapq.heappush(heap, (-s, idx))

        cnt = 1
        arr = [None] * len(score)
        while heap:
            _, idx = heapq.heappop(heap)
            if cnt == 1:
                 arr[idx] = "Gold Medal"
            elif cnt == 2:
                 arr[idx] = "Silver Medal"
            elif cnt == 3:
                 arr[idx] = "Bronze Medal"
            else:
                 arr[idx] = str(cnt)
            cnt += 1
        return arr
