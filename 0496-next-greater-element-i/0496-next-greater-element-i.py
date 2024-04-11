class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for i in nums2:
            while stack and stack[-1] < i:
                x = stack.pop()
                dic[x] = i
            stack.append(i)
        for idx, n in enumerate(nums1):
            if n in dic:
                nums1[idx] = dic[n]
            else:
                nums1[idx] = -1
        return nums1
