# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        dic = {}
        arr = []
        def dfs(node: TreeNode):
            dic[node.val] = ''.join(arr)
            if node.left:
                arr.append('L')
                dfs(node.left)
                arr.pop()
            if node.right:
                arr.append('R')
                dfs(node.right)
                arr.pop()
        dfs(root)
        startPath = dic[startValue]
        destPath = dic[destValue]
        while len(startPath) > 0 and len(destPath) > 0 and startPath[0] == destPath[0]:
            startPath = startPath[1:]
            destPath = destPath[1:]
        return startPath.replace('L', 'U').replace('R', 'U') + destPath
