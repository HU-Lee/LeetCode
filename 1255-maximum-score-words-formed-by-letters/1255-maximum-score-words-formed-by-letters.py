class Solution:
    ans = 0
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        l = len(words)
        counts = [0 for _ in range(26)]
        for lett in letters:
            counts[ord(lett)-ord('a')] += 1

        def dfs(x):
            val = 0
            if x >= l:
                return val
            else:
                w = words[x]
                wc = [w.count(chr(ord('a') + i)) for i in range(26)]
                
                if all(wc[i] <= counts[i] for i in range(26)):
                    for i in range(26):
                        counts[i] -= wc[i]
                    val = sum(wc[i]*score[i] for i in range(26)) + dfs(x+1)
                    for i in range(26):
                        counts[i] += wc[i]
                val = max(val, dfs(x+1))
                self.ans = max(self.ans, val)
                return val
        
        for i in range(l):
            dfs(i)
        return self.ans