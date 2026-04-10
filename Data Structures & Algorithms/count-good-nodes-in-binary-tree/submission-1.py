# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node,greater):
            if not node:
                return
            if node.val>=greater.val:
                self.count = self.count +1
                greater = node
            dfs(node.left,greater)
            dfs(node.right,greater)
            return
        dfs(root,root)
        return self.count