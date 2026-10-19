class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        memo = {}

        def traverse(index, memo):

            if index >= len(costs):
                return 0

            if index in memo:
                return memo[index] + costs[index]

            # print(index, cost)

            # cost += costs[index]

            min_cost = min(traverse(index+1, memo), traverse(index+2, memo))

            memo[index] = min_cost
            return costs[index] + min_cost
        
        # cost = 0
        # # print(traverse(1, cost))
        # cost1 = traverse(0, cost)
        # cost = 0
        # cost2 = traverse(0, cost)
        # print(traverse(0, 0))
        # print(traverse(1, 0))
        minimum = min(traverse(0,  {}), traverse(1, {}))

        return minimum

        