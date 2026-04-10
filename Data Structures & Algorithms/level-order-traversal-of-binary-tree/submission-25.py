# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#        l = []
#        l.add(1)
#        for i in range(len(l)):
#            i = l.pop(0)
#            l.add(i.left)
#            l.add(i.right)
#            print(i)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        output = []

        if not root: return []
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                n = queue.pop(0) 
                level.append(n.val)
                if n.left:
                    queue.append(n.left) 
                if n.right:
                    queue.append(n.right) 
            output.append(level)
        return output
         





    