class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        not_found_sum = (m+n)*mean - sum(rolls)
        if not_found_sum < n or not_found_sum > 6 * n:
            return []
        
        x, r = not_found_sum // n, not_found_sum % n
        return [(x+1)]*r + [x] * (n-r)