class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        table = [(num, num) for num in nums]

        for i in range(2, len(nums)):
            maximum = 0

            for j in range(i - 2, -1, -1):
                maximum = max(table[j][1], maximum)

            table[i] = (table[i][0], table[i][0] + maximum)

        return max(table[-1][1], table[-2][1])

