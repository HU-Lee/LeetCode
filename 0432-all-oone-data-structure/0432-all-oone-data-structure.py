class AllOne:
    def __init__(self):
        self.data = defaultdict(int)
        self.counts = defaultdict(set)
        self.min = 0
        self.max = 0
        self.total_data = 0

    def inc(self, key: str) -> None:
        self.total_data += 1
        prev_count = self.data[key]
        # Discard has also O(1) complexity
        self.counts[prev_count].discard(key)
        self.counts[prev_count+1].add(key)
        self.data[key] += 1

        if self.total_data == 1:
            self.max = 1
            self.min = 1
            return
        if prev_count == self.max:
            self.max += 1
        if (prev_count + 1 < self.min) or \
           (prev_count == self.min and not self.counts[prev_count]):
            self.min = prev_count + 1

    def dec(self, key: str) -> None:
        self.total_data -= 1
        prev_count = self.data[key]
        self.counts[prev_count].discard(key)
        if prev_count > 1:
            self.counts[prev_count-1].add(key)
        self.data[key] -= 1

        if self.total_data == 0:
            self.max = 0
            self.min = 0
            return
        if prev_count == self.max and not self.counts[prev_count]:
            self.max -= 1
        if prev_count == self.min and not self.counts[prev_count]:
            self.min = max(prev_count-1, 0)
        
    def getMaxKey(self) -> str:
        return next(iter(self.counts[self.max]), "")

    def getMinKey(self) -> str:
        return next(iter(self.counts[self.min]), "")
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()