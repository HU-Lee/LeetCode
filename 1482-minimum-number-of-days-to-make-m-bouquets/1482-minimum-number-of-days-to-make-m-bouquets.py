class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        
        mi, mx = min(bloomDay), max(bloomDay)
        ans = mx

        while mi <= mx:
            mid = (mi + mx) // 2
            cnt = 0
            stack = 0
            for b in bloomDay:
                if b <= mid:
                    stack += 1
                else:
                    stack = 0
                if stack >= k:
                    stack = 0
                    cnt += 1
            if cnt >= m:
                ans = min(ans, mid)
                mx = mid - 1
            else:
                mi = mid + 1
            
        return ans