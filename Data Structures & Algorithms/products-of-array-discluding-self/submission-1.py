class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_suffix = []
        results = []
        result = 1
        ## count prefixes for each one
        for i in range(len(nums)):
            if i == 0:
                prefix_suffix.append([1, 0])
            else:
                tup = [prefix_suffix[i - 1][0] * nums[i-1], 0]
                prefix_suffix.append(tup)

        ## count postfixes for each one
        for i in range(len(nums) -1 , -1, -1):
            if i == len(nums) - 1:
                prefix_suffix[i][1] = 1
            else:
                # tup = (prefix_suffix[i - 1][1] * nums[i+1], 0)
                posfix = prefix_suffix[i + 1][1] * nums[i+1]

                prefix_suffix[i][1] = posfix
                # prefix_suffix.append(tup)

        for i in range(len(prefix_suffix)):
            value = prefix_suffix[i][0] * prefix_suffix[i][1]
            results.append(value)

        return results



            

        return results