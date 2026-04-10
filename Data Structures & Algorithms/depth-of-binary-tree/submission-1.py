# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(node,level):
            
            if not node:
                return level

            res = max(getDepth(node.left,level+1),getDepth(node.right,level+1))
            return res
        return getDepth(root,0)