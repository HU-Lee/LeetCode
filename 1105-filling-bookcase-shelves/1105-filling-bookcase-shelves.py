class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dps = [0]*n
        dps[0] = books[0][1]

        for i in range(1, n):
            dps[i] = dps[i-1] + books[i][1]
            tmpWidth = 0
            maxHeight = 0
            for k in range(i, -1, -1):
                tmpWidth += books[k][0]
                if shelfWidth < tmpWidth:
                    break
                maxHeight = max(maxHeight, books[k][1])
                if k == 0:
                    dps[i] = maxHeight
                else:
                    dps[i] = min(dps[i], dps[k-1] + maxHeight)
        
        return dps[-1]