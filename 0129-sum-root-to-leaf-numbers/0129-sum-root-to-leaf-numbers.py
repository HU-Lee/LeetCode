# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        path = []

        def dfs(nd):
            if not nd:
                return 0
            elif not (nd.left or nd.right):
                path.append(nd.val)
                val = sum((x*(10**(len(path)-1-i)) for i, x in enumerate(path)))
                path.pop()
                return val
            else:
                path.append(nd.val)
                val = dfs(nd.left) + dfs(nd.right)
                path.pop()
                return val
        
        return dfs(root)