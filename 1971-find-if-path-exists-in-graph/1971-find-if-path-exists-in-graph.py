import collections

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited = [False for _ in range(n)]

        q = [source]
        visited[source] = True
        while q:
            x = q.pop()
            if x == destination:
                return True
            for t in graph[x]:
                if not visited[t]:
                    visited[t] = True
                    q.append(t)
        return False