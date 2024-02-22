class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_from = {}
        trust_to = {}
        for t in trust:
            trust_from[t[0]] = 1
            trust_to[t[1]] = trust_to.get(t[1],0) + 1
        for i in range(1,n+1):
            if trust_from.get(i,0) == 0 and trust_to.get(i,0) == n-1:
                return i
        return -1