# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def isDeleteTarget(node):
            return node and node.val == target and node.left is None and node.right is None

        def parseNodes(node):
            if node is None:
                return node
            node.left = parseNodes(node.left)
            node.right = parseNodes(node.right)
            if isDeleteTarget(node.left):
                node.left = None
            if isDeleteTarget(node.right):
                node.right = None
            return node

        parsed = parseNodes(root)
        return None if isDeleteTarget(root) else parsed