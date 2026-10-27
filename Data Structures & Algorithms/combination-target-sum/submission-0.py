class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        def createTuple(combination):

            arr = [0] * len(nums)
            values = []
            for index in combination:
                values.append(nums[index])
                arr[index] += 1

            return tuple(arr), values


        hash_set = set()
        combinations = []
        def combinate(target, combination_indices):
            if target == 0:
                tup, combination = createTuple(combination_indices)
                if tup not in hash_set:
                    hash_set.add(tup)
                    combinations.append(combination)
                return True
            if target < 0:
                return False

            for i in range(len(nums)):
                num = nums[i]
                isGood = len(combination_indices) == 0 or num >= nums[combination_indices[len(combination_indices) - 1]]
                
                if isGood:
                    # combination.append(num)
                    combination_indices.append(i)
                    combinate(target - num, combination_indices)
                    combination_indices.pop()
                    # combination.pop()
            
        combinate(target,  [])
        return combinations