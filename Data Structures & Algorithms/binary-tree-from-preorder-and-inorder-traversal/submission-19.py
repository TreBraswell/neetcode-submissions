# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def reorganize(pre,ino,dire):

            print(pre,ino,dire)
            if len(pre) == 0 or len(ino) == 0:
                return None
            t = TreeNode(pre[0])
            m = ino.index(pre[0])
            t.left = reorganize(pre[1:m+1],ino[0:m],"left")
            print("pop out ",pre,ino)
            t.right = reorganize(pre[1+m:],ino[m+1:],"right")
            return t
        return reorganize(preorder,inorder,"left")