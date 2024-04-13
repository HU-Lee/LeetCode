class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        st = []
        bd_right = [i for i in range(l)]
        for idx, h in enumerate(heights):
            while st and st[-1][0] > h:
                x,i = st.pop()
                bd_right[i] = idx-1
            st.append((h, idx))
        while st:
            x,i = st.pop()
            bd_right[i] = l-1
        bd_left = [i for i in range(l)]
        for idx, h in enumerate(heights[::-1]):
            while st and st[-1][0] > h:
                x,i = st.pop()
                bd_left[i] = l-idx
            st.append((h, l-1-idx))
        while st:
            x,i = st.pop()
            bd_left[i] = 0

        ans = 0
        for i in range(l):
            tmp = heights[i]*(bd_right[i] - bd_left[i] + 1)
            ans = max(ans, tmp)
        return ans
