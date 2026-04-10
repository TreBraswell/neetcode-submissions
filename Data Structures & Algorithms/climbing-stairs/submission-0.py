class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1
        result = first
        for n in range(n-2,-1,-1):

            temp = first + second
            second = first
            first = temp
        return first
