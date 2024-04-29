class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        caps = list(reversed(sorted(capacity)))
        x = 0
        while apples > 0:
            apples -= caps[x]
            x += 1
        return x 