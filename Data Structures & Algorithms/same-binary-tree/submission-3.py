# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def sametree(node1,node2):
            if not node1 and not node2:
                return True
            elif node1 and node2 and node1.val == node2.val:
                return sametree(node1.right,node2.right) and sametree(node1.left,node2.left)
            else:
                return False
        def dfs(p,q):
            if not p and  not q:
                return True
            elif p and q:
                return sametree(p,q) and dfs(p.right,q.right) and dfs(p.left,q.left)
            else:
                return False
        return dfs(p,q)
