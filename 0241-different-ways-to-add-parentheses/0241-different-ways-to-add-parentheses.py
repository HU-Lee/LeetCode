class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if len(expression) <= 2:
            return [int(expression)]

        ans = []

        for idx, val in enumerate(expression):
            if val in "+-*":
                left_compute = self.diffWaysToCompute(expression[:idx])
                right_compute = self.diffWaysToCompute(expression[idx+1:])
                for i in left_compute:
                    for j in right_compute:
                        if val == "+":
                            ans.append(i+j)
                        elif val == "-":
                            ans.append(i-j)
                        elif val == "*":
                            ans.append(i*j)
        return ans



