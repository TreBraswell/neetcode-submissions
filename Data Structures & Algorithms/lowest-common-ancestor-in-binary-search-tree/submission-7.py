# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            print('this is ',node.val)
            if node.val> p.val and node.val>q.val:
                print('we went here')
                return dfs(node.left)
            elif node.val<p.val and node.val<q.val:
                print('we didnt go here')
                return dfs(node.right)
            else:
                return node
        return dfs(root)