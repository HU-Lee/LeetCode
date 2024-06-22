class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        cnt = 0
        for num in nums:
            if num % 2 == 1:
                cnt += 1
            dic[cnt] += 1
        ans = 0
        for key in range(cnt-k+1):
            ans += dic[key]*dic[key+k]
        return ans