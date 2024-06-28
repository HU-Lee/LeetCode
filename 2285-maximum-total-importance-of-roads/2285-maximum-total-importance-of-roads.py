class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        city_roads = [0]*n
        for x, y in roads:
            city_roads[x] += 1
            city_roads[y] += 1
        
        cnts = collections.Counter(city_roads)
        base = 1
        ans = 0
        for x, y in sorted(cnts.items()):
            ans += x * (base + (base + y - 1)) * y // 2
            base += y
        return ans