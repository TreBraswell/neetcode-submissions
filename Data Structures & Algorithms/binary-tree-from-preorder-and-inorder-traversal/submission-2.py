# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #check if our arrays exist
        if not preorder or not inorder:
            return None
        #find first node
        root = TreeNode(preorder[0])
        #then find middle index
        mid = inorder.index(preorder[0])
        # move middle index between them with preorder
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1 :])
        return root
            