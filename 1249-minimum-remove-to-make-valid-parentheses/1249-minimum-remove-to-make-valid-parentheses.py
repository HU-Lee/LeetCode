class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        err_open = []
        err_close = []
        for idx, x in enumerate(s):
            if x == "(":
                err_open.append(idx)
            elif x == ")":
                if not err_open:
                    err_close.append(idx)
                else:
                    err_open.pop()
        
        for idx, x in enumerate(s):
            if idx not in err_open + err_close:
                ans += x

        return ans