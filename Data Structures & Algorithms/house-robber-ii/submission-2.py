class Solution:
    def rob(self, nums: List[int]) -> int:
        memo1 ={}
        memo2 ={}


        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0

        def traverse(index, fromZero, memo):
            current = nums[index]
            maximum = 0
            if index in memo:
                return memo[index]

            length = len(nums) - 1 if fromZero else len(nums)
            for i in range(index + 2, length):
                maximum = max(maximum, traverse(i, fromZero, memo))
            
            memo[index] = maximum + current
            return memo[index]
        
        from_zero = traverse(0,  True, memo1)
        from_one = traverse(1,  False, memo2)
        from_second = traverse(2,  False, memo2) if len(nums) > 2 else 0


        return max(max(from_zero, from_one), from_second)

