class Solution:
    def rob(self, nums: List[int]) -> int:
        memo ={}

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0

        def traverse(index, memo, fromZero):
            current = nums[index]
            maximum = 0
            if index in memo:
                return memo[index]

            length = len(nums) - 1 if fromZero else len(nums)
            for i in range(index + 2, length):
                maximum = max(maximum, traverse(i, memo, fromZero))
            
            memo[index] = maximum + current
            return memo[index]
        
        from_zero = traverse(0, memo, True)
        from_one = traverse(1, memo, False)
        from_end = traverse(len(nums) - 1, memo, False)


        return max(max(from_zero, from_one), from_end)

