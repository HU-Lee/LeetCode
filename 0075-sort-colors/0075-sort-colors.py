class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]
        for num in nums:
            colors[num] += 1
        color,idx = 0,0
        while color < 3:
            if colors[color] == 0:
                color += 1
                continue
            colors[color] -= 1
            nums[idx] = color
            idx += 1