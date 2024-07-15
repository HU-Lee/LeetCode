# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        children = set()
        for p, c, left in descriptions:
            # setdefault returns value, or inserts the default value if not exists.
            pNode = nodes.setdefault(p, TreeNode(p))
            cNode = nodes.setdefault(c, TreeNode(c))
            if left == 1:
                pNode.left = cNode
            else:
                pNode.right = cNode
            children.add(c)
        root = [x for x, _, _ in descriptions if x not in children]
        return nodes[root[0]]