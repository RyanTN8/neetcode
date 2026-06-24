class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            print("lt2")
            return min(cost)

        steps = [0] * (len(cost) + 1)

        for i in range(2, len(steps)):
            steps[i] = min(steps[i - 2] + cost[i - 2], steps[i - 1] + cost[i - 1])
            
        return steps[-1]