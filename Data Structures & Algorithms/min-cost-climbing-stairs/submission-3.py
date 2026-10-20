class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        memo ={}
        def traverse(index):

            if index >= len(costs):
                return 0

            if index in memo:
                return memo[index] + costs[index]


            min_cost = min(traverse(index+1), traverse(index+2))

            memo[index] = min_cost
            return costs[index] + min_cost
        
        minimum = min(traverse(0), traverse(1))

        return minimum

        