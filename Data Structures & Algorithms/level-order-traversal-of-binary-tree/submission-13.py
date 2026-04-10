# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_queue = []
        if not root:
            return []
        level_queue.append(root)
        result = []
        while level_queue:
            level = []
            for i in range(len(level_queue)):
                node = level_queue.pop(0)
                if not node:
                    continue
                level.append(node.val)
                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
            result.append(level)
        return result
