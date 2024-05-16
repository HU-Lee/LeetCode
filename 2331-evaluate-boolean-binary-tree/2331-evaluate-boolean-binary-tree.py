# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def andor(x,y,c) -> int:
            if c == 2:
                return 1 if x+y>0 else 0
            else:
                return x*y

        def dfs(node: TreeNode) -> int:
            if node.val < 2:
                return node.val
            else:
                return andor(dfs(node.left), dfs(node.right), node.val)

        return dfs(root) == 1

