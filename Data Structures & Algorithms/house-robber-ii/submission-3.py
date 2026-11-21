class Solution:
    def rob(self, nums: List[int]) -> int:
        LENGTH = len(nums)

        if LENGTH == 1:
            return nums[0]
        if LENGTH == 2:
            return max(nums[0], nums[1])

        table = [(nums[i], nums[i], 0 if i == 0 else nums[i]) for i in range(LENGTH)]

        for i in range(2, LENGTH):
            maximum_with = 0
            maximum_without = 0

            for j in range(i - 2, -1, -1):
                maximum_with = max(table[j][1], maximum_with)
                maximum_without = max(table[j][2], maximum_without)

            table[i] = (table[i][0], table[i][1] + maximum_with, table[i][2] + maximum_without)
        

        return max(max(table[-1][2], table[-2][1]), table[-3][1])


[100, 4, 3, 80, 70, 30] 