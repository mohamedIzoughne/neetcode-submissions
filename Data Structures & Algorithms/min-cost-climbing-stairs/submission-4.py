class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:

        new_costs = [(costs[i], 0) if i not in [0, 1] else (costs[i], costs[i]) for i in range(len(costs))]

        for i in range(2, len(new_costs)):
            minimum = min(new_costs[i - 1][1], new_costs[i - 2][1])
            new_costs[i] = (new_costs[i][0],  new_costs[i][0] + minimum)
        
        return min(new_costs[-1][1], new_costs[-2][1])

