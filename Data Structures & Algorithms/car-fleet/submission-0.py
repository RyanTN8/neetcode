class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i], speed[i], (target - position[i]) / speed[i] ] for i in range(len(position))]
        cars.sort(key = lambda x: -x[0])

        stack = []
        for i in range(len(cars)):
            if not stack or cars[i][2] > stack[-1]:
                stack.append(cars[i][2])
        return len(stack)
                


