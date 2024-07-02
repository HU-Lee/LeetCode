class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1, a2 = 0,0
        nums1.sort()
        nums2.sort()
        arr = []
        while a1 < len(nums1) and a2 < len(nums2):
            if nums1[a1] == nums2[a2]:
                arr.append(nums1[a1])
                a1 += 1
                a2 += 1
            elif nums1[a1] > nums2[a2]:
                a2 += 1
            else:
                a1 += 1
        return arr