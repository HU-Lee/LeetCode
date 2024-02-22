class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_froms = list(set([x[0] for x in trust]))
        if len(trust_froms) != n-1:
            return -1
        else:
            possible = n*(n+1)//2 - sum(trust_froms)
            if all([x,possible] in trust for x in trust_froms):
                return possible
            else:
                return -1 
        