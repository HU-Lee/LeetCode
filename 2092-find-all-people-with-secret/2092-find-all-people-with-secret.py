import heapq
import collections

class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        time = 0
        ans = {0, firstPerson}
        meeting_times = collections.defaultdict(list)
        for x,y,t in meetings:
            meeting_times[t].append((x,y))
        
        visited = {}    
        def add_dfs(k, g):
            visited[k] = True
            ans.add(k)
            for t in g[k]:
                if t not in visited:           
                    add_dfs(t, g)

        for t in sorted(meeting_times.keys()):
            g = collections.defaultdict(list)
            for x,y in meeting_times[t]:
                g[x].append(y)
                g[y].append(x)
            for k in g.keys():
                if k in ans:
                    add_dfs(k, g)

        return list(ans)
