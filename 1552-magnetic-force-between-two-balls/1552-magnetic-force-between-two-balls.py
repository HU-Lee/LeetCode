class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        l = len(position)
        position.sort()
        ans = 0

        # Magnetic force range
        mi = 1
        mx = position[-1] // (m-1)

        # Binary...
        while mi <= mx:
            mid = (mi + mx) // 2
            base = position[0]
            balls = 1
            for i in range(1, l):
                if position[i] - base >= mid:
                    balls += 1
                    base = position[i]
            if balls >= m:
                ans = mid
                mi = mid + 1
            else:
                mx = mid -1
        return ans