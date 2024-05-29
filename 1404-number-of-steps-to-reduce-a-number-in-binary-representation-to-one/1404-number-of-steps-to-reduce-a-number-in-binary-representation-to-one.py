class Solution:
    def numSteps(self, s: str) -> int:
        cnt = 0
        curr = list(reversed(list(map(int, list(s)))))

        while len(curr) > 1:
            if curr[0] == 0:
                curr = curr[1:]
            else:
                curr[0] = 0
                for i in range(1, len(curr)+1):
                    if i == len(curr):
                        curr.append(1)
                        break
                    if curr[i] == 1:
                        curr[i] = 0
                    else:
                        curr[i] = 1
                        break
            cnt += 1

        return cnt