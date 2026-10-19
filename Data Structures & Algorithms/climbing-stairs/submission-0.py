class Solution:
    def climbStairs(self, n: int) -> int:
        

        def traverse(n, memo={}):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            
            if n in memo:
                return memo[n]

            memo[n] = traverse(n-1, memo) + traverse(n-2, memo)

            return memo[n]

        return traverse(n)