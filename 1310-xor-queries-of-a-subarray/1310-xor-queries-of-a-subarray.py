class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]

        ans = []
        for left, right in queries:
            ans.append(prefix[left] ^ prefix[right+1])
        return ans