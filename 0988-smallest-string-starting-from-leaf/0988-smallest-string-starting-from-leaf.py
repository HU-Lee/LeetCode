# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        mi = ["X"]
        arr = []

        def dfs(node):
            if not node:
                return
            if not (node.left or node.right):
                arr.append(alphabets[node.val])
                s = "".join(arr[::-1])
                x = mi[0]
                if x == "X" or x > s:
                    mi[0] = s
                arr.pop()
            else:
                arr.append(alphabets[node.val])
                dfs(node.left)
                dfs(node.right)
                arr.pop()
        
        if root.left or root.right:
            dfs(root)
            return mi[0]
        else:
            return root.val
