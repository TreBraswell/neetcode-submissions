class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        def rob_the_house(to_rob):
            first = 0
            second = 0
            # if len(to_rob) == 1:
            #     return to_rob[0]
            # if len(to_rob) == 2:
            #     return max(to_rob[0],to_rob[1])
            first = to_rob[0]
            second = max(to_rob[1],to_rob[0])
            for i in range(2, len(to_rob)):
                print( first,second,to_rob[i])
                temp = max(to_rob[i]+first, second)
                first = second
                second = temp
            return max(first, second)
        return max(nums[0], rob_the_house(nums[1:]),rob_the_house(nums[:-1]))