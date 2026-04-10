# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0,0]
            l = dfs(node.left)
            r = dfs(node.right)
            choose = node.val + l[1] + r[1]
            dont_choose = max(l) + max(r)
            return [choose,dont_choose]
        return max(dfs(root))