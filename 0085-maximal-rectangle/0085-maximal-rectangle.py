class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rect = 0



        def maxHistogram(histogram: List[int]) -> int:
            l = len(histogram)
            ans = 0
            st = []
            for idx, h in enumerate(histogram):
                start = idx
                while st and st[-1][0] > h:
                    x,i = st.pop()
                    ans = max(ans, x*(idx - i))
                    start = i
                st.append((h, start))
            for x,i in st:
                ans = max(ans, x*(l-i))
            return ans

        arr = [0 for _ in matrix[0]]
        for m in matrix:
            for i in range(len(arr)):
                if m[i] == '1':
                    arr[i] += 1
                else:
                    arr[i] = 0
            rect = max(rect, maxHistogram(arr))
        return rect