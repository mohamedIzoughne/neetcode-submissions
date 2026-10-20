class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}
        n = len(cost)

        def min_cost(i: int) -> int:
            # Base case: reaching or passing the top (past the last index)
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            # Cost to pay at step i + best choice for the next move
            memo[i] = cost[i] + min(min_cost(i + 1), min_cost(i + 2))
            return memo[i]

        # The problem allows starting at index 0 or index 1
        return min(min_cost(0), min_cost(1))