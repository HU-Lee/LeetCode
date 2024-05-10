class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = len(arr)
        heap = []
        for i in range(l):
            for j in range(i+1, l):
                heapq.heappush(heap, (float(arr[i])/arr[j], arr[i], arr[j]))
        
        x,y = 0,0
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
        
        return [x,y]