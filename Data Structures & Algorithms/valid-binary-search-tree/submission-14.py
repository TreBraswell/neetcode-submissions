# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,small,great):
            if not node:
                return True
            l = True
            r = True
            if small>=node.val or great<=node.val:
                return False
            return dfs(node.left,small,min(great,node.val)) and dfs(node.right,max(small,node.val),great)   
            # small = min(small,node.val)
            # great = max(great,node.val) 
            
        return dfs(root,float('-inf'),float('inf'))
