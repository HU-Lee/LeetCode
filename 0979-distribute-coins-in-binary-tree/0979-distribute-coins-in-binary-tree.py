# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        # amount of coins to move (node -> parent), can be minus
        def count(node):
            if node==None: return 0
            left = count(node.left)
            right = count(node.right)
            self.ans += abs(left) + abs(right)
            return node.val + left + right - 1
        
        count(root)
        return self.ans