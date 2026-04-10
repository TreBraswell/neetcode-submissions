class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml = 0
        mr = len(matrix)-1
        full_break = False
        while ml<=mr:
            mm = int(ml + (mr - ml)/2)
            print(mm,ml,mr)
            if matrix[mm][0] > target:
                mr = mm - 1
            elif matrix[mm][len(matrix[0]) - 1] < target:
                ml = mm + 1
            else:
                full_break = True
                break

        print('passed full_break')
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = int(l + ((r - l) / 2) )
            if matrix[mm][m] > target:
                r = m - 1
            elif matrix[mm][m] < target:
                l = m + 1
            else:
                return True
        return False
        
