class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0] * (n)
        if n == 1:
            return 1
            
        table[0] = 1
        table[1] = 1

        for i in range(n - 1):
            table[i + 1] += table[i]
            if i + 2 < n:
                table[i + 2] += table[i]
        return table[-1]
