class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for idx, num in enumerate(arr2):
            dic[num] = idx - 2000

        ans = sorted(arr1, key = lambda x: dic.get(x,x)) 
        return ans