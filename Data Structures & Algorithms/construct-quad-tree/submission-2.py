"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(row,col,n):
            
            if n == 1:
                print('is one',row,col,n)
                return Node(grid[row][col],True)
            
            
            h= n//2
            # print('doing dfs')
            top_left = dfs(row,col,h)
            top_right = dfs(row,col+h,h)
            bottom_left = dfs(row+h,col,h)
            bottom_right = dfs(row+h,col+h,h)

            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf:
                if top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                    # print('is same after dfs',row,col,n)
                    return Node(top_left.val,True)
            # print('not same',row,col,n)
            return Node(1,False,top_left,top_right,bottom_left,bottom_right)
        return dfs(0,0,len(grid))

