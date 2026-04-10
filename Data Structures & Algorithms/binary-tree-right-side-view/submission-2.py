# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       que = [] 
       output = []

       if not root: return []

       que.append(root)
       while que:
        level = []
        for q in range(len(que)):
            n = que.pop(0)
            level.append(n.val)
            if n.left: que.append(n.left)
            if n.right: que.append(n.right)
        output.append(level.pop())
       return output
        



