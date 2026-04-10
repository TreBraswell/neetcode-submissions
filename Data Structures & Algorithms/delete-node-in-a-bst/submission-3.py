# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val> key:
            root.left = self.deleteNode(root.left,key)
        elif root.val<key:
            root.right = self.deleteNode(root.right,key)
        else:
            node = root
            if not node.left and not node.right:
                return None
            if not node.right:
                return node.left
            if not node.left:
                return node.right     
            nxt = root.right
            while nxt.left:
                nxt = nxt.left
            root.val = nxt.val
            root.right =self.deleteNode(root.right,nxt.val)
        return root