class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = ""
        cnt = 0
        for x in s:
            if x == "(":
                cnt += 1
            elif x == ")":
                cnt -= 1
            if cnt < 0:
                cnt = 0
                continue
            tmp += x
        
        ans = ""
        cnt = 0
        for x in reversed(tmp):
            if x == ")":
                cnt += 1
            elif x == "(":
                cnt -= 1
            if cnt < 0:
                cnt = 0
                continue
            ans = x + ans

        return ans