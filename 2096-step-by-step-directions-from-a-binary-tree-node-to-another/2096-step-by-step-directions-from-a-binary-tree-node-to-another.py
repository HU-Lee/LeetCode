# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(node: TreeNode, value: int):
            if node.left:
                ans = findPath(node.left, value)
                if ans is not None:
                    return 'L' + ans
            if node.right:
                ans = findPath(node.right, value)
                if ans is not None:
                    return 'R' + ans
            return '' if node.val == value else None

        startPath = findPath(root, startValue)
        destPath  = findPath(root, destValue)
        while len(startPath) > 0 and len(destPath) > 0 and startPath[0] == destPath[0]:
            startPath = startPath[1:]
            destPath = destPath[1:]
        return startPath.replace('L', 'U').replace('R', 'U') + destPath
