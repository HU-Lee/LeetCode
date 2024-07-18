# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        paths = set()
        arr = []
        def dfs(node: TreeNode):
            if not node.left and not node.right:
                paths.add(''.join(arr))
                return
            if node.left:
                arr.append('L')
                dfs(node.left)
                arr.pop()
            if node.right:
                arr.append('R')
                dfs(node.right)
                arr.pop()

        def get_dist(a: str, b: str):
            t1, t2 = a,b
            while len(t1) > 0 and len(t2) > 0 and t1[0] == t2[0]:
                t1, t2 = t1[1:], t2[1:]
            return len(t1) + len(t2)

        dfs(root)

        paths = sorted(list(paths))
        ans = 0
        for i in range(len(paths)):
            for j in range(i+1, len(paths)):
                if get_dist(paths[i], paths[j]) <= distance:
                    ans += 1
        return ans