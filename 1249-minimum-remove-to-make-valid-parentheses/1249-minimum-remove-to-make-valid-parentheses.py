class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        arr = []
        for idx, x in enumerate(l):
            if x == "(":
                arr.append(idx)
            elif x == ")":
                if arr:
                    arr.pop()
                else:
                    l[idx] = ''
        
        for i in arr:
            l[i] = ''

        return ''.join(l)