class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in  range(n)]
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        ends = [i for i in range(n) if len(graph[i]) == 1]
        
        processed = 0
        while n-processed > 2:
            new_ends = []
            for e in ends:
                for k in graph[e]:
                    arr = graph[k]
                    arr.remove(e)
                    if len(arr) == 1:
                        new_ends.append(k)
            processed += len(ends)
            ends = new_ends

        return ends

