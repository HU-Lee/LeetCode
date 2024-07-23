class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        arr = [0] * 201
        for num in nums:
            arr[num+100] += 1
        listup = sorted(
            [(arr[i], i-100) for i in range(201) if arr[i] != 0 ],
            key=lambda x: (x[0], -x[1])
        )
        ans = []
        for cnt, val in listup:
            ans += [val] * cnt
        return ans