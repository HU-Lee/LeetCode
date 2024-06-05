class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = collections.defaultdict(int)
        for s in words[0]:
            letters[s] += 1
        
        for i in range(1, len(words)):
            tmp = collections.defaultdict(int)
            for s in words[i]:
                tmp[s] += 1
            for key in letters.keys():
                letters[key] = min(letters[key], tmp[key])
        
        ans = []
        for key, val in letters.items():
            ans += [key]*val
        return ans