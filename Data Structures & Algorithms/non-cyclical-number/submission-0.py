class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def check(b):
            res = 0
            while b != 0:
                t = b%10
                t = t **2
                b = b //10
                res+=t
            return res
        while n!= 1:
            visited.add(n)
            n = check(n)
            if n in visited:
                return False
        return True
        