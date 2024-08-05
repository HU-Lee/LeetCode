class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = []
        overall = set()

        for word in arr:
            if word in overall:
                distinct = list(filter(lambda x: x != word, distinct))
            else:
                distinct.append(word)
            overall.add(word)
        
        if k > len(distinct):
            return ''
        else:
            return distinct[k-1]
