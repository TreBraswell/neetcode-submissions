class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 0
        for i in range(n,-1,-1):
            third = first + second
            temp = second 
            second= third
            first = temp
            print(first,second)
        return second