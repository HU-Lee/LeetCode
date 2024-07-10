class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for l in logs:
            if l == './':
                continue
            elif l == '../':
                depth = max(depth-1, 0)
            else:
                depth += 1
        return depth