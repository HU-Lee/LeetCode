class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        idxs = [i for i in range(len(deck))]
        arr = []
        while idxs:
            x = idxs.pop(0)
            arr.append(x)
            if idxs:
                y = idxs.pop(0)
                idxs.append(y)
        ans = [-1 for _ in range(len(deck))]
        for idx, i in enumerate(arr):
            ans[i] = deck[idx]
        return ans