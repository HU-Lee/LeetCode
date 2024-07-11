class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        cur = list(s)
        for idx, l in enumerate(s):
            if l == '(':
                stack.append(idx)
            elif l == ')':
                prev = stack.pop()
                cur = cur[:prev] + cur[prev:idx][::-1] + cur[idx:]
        
        return ''.join(list(filter(lambda x: x not in ['(', ')'], cur)))