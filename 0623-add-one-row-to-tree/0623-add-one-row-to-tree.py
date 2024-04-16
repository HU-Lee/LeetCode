# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def work(node: Optional[TreeNode], d: int):
            if not node:
                return
            if d == depth-1:
                x = node.left
                n = TreeNode(val, x, None)
                node.left = n
                x = node.right
                n = TreeNode(val, None, x)
                node.right = n
                return
            else:
                work(node.left, d+1)
                work(node.right, d+1)
        
        if depth == 1:
            return TreeNode(val, root, None)
        work(root, 1)
        return root