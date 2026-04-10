# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(p,q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                l = sametree(p.left,q.left)
                r = sametree(p.right,q.right)
                return l and r
            else:
                return False
        def dfs(node):
            if not node:
                return False 
            res = sametree(node,subRoot)
            l = dfs(node.left)
            r = dfs(node.right)           
            return res or l or r
        return dfs(root)
                