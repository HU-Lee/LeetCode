class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = ""
        tmp = ""
        rootFound = False
        for l in sentence:
            if l == " ":
                ans += tmp + l
                tmp = ""
                rootFound = False
            elif rootFound:
                continue
            else:
                tmp += l
                if tmp in dictionary:
                    rootFound = True
        ans += tmp
        return ans
                
