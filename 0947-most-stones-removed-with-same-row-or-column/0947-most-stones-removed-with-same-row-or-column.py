class Solution:
    distinct = 0

    def removeStones(self, stones: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(stones)
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False] * n

        def visit(i):
            visited[i] = True
            for k in graph[i]:
                if not visited[k]:
                    visit(k)
        
        for i in range(n):
            if not visited[i]:
                self.distinct += 1
            visit(i)
        
        return n - self.distinct