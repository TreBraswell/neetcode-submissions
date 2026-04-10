class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort()
        stack = []

        for p, s in reversed(cars):
            time = (target - p) / s
            if len(stack) == 0:
                stack.append(time)
            else:
                if stack[-1] < time:
                    stack.append(time)

        return len(stack)


        
