class Solution:
    def rob(self, nums: List[int]) -> int:
        memo ={}

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0

        def traverse(index,  memo):
            current = nums[index]
            maximum = 0
            if index in memo:
                return memo[index]

            for i in range(index + 2, len(nums)):
                maximum = max(maximum, traverse(i, memo))
            
            memo[index] = maximum + current
            return memo[index]
        
        from_zero = traverse(0,  memo)
        from_one = traverse(1,  memo)

        return max(from_zero, from_one)
                

