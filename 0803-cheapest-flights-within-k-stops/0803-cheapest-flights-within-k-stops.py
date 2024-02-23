import heapq
import collections

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # Parse
        graph = collections.defaultdict(list)
        for f,t,p in flights:
            graph[f].append((t,p))
        
        # Init
        max_paths = [k]*n
        max_paths[src] = 0
        price_q = sorted([(p, 0, d) for d,p in graph[src]])

        while price_q:
            # Get minimum price
            price, stop, dest = heapq.heappop(price_q)
            if stop <= k and dest == dst:
                return price
            # Multiple visit is possible, but stop needs to be lower than previous visit.
            # Already lower price with this destination is passed, so possibility only exists on less stop.
            if stop < max_paths[dest]:            
                # Mark
                max_paths[dest] = stop
                for t,p in graph[dest]:
                    heapq.heappush(price_q, (price+p, stop+1, t))

        return -1


