class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f, t = 0,0
        success = True
        for bill in bills:
            if bill == 5:
                f += 1
            elif bill == 10:
                if f <= 0:
                    success = False
                    break
                f -= 1
                t += 1
            else:
                if t <= 0:
                    if f >= 3:
                        f -= 3
                    else:
                        success = False
                        break
                else:
                    if f > 0:
                        f -= 1
                        t -= 1
                    else:
                        success = False
                        break

        return success
