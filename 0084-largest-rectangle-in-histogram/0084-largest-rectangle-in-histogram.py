class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        ans = 0
        st = []
        for idx, h in enumerate(heights):
            start = idx
            while st and st[-1][0] > h:
                x,i = st.pop()
                ans = max(ans, x*(idx - i))
                start = i
            st.append((h, start))
        for x,i in st:
            ans = max(ans, x*(l-i))
        return ans
