class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Solve with bit...
        # counts of strings with prefix
        count = defaultdict(int)
        
        # empty string
        count[0] = 1

        ans = 0
        prefix = 0

        for w in word:
            prefix ^= (1 << (ord(w)-ord('a')))

            ## all even
            ans += count[prefix]

            ## one odd
            for i in range(10):
                ans += count[prefix ^ 1 << i]
            count[prefix] += 1

        return ans

