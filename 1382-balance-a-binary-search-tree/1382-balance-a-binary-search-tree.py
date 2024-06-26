# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []

        # Add values to the array
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        
        dfs(root)

        # Get tree by cutting half
        def getTree(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            return TreeNode(
                values[mid],
                getTree(left, mid - 1),
                getTree(mid + 1, right)
            )
        
        return getTree(0, len(values) - 1)
