# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def sumNode(node):
            if node is None:
                return 0
            return sumNode(node.left) + sumNode(node.right) + node.val
        
        def newNode(node, carry):
            if node is None:
                return None
            rightSum = sumNode(node.right)
            node.right = newNode(node.right, carry)
            node.val += rightSum + carry
            node.left = newNode(node.left, node.val)
            return node

        return newNode(root, 0)