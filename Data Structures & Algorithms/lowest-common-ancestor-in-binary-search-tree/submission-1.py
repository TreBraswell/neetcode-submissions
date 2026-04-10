# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            v = root.val
            if v<p.val and v<q.val:
                root = root.right
            elif v>p.val and v>q.val:
                root = root.left
            else:
                return root