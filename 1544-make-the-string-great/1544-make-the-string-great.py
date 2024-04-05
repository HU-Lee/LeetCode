class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        for i in s:
            if arr and arr[-1] != i and (arr[-1].upper() == i or arr[-1].lower()==i):
                arr.pop()
            else:
                arr.append(i)
        return "".join(arr)
        