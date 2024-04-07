class Solution:
    def checkValidString(self, s: str) -> bool:
        coins = []
        opens = []
        for i, x in enumerate(s):
            if x == '*':
                coins.append(i)
            elif x == '(':
                opens.append(i)
            else:
                if opens:
                    opens.pop()
                elif coins:
                    coins.pop()
                else:
                    return False
        while opens:
            o = opens.pop()
            if coins and coins.pop() > o:
                continue
            else:
                return False
        return True