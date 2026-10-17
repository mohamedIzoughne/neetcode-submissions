class Solution:

    def twoSum(self, key, nums, target):
        dic = {}
        result = []
        value = nums[key]
        for i in range(len(nums)):
            num = nums[i]
            if i != key:
                dic[target - num] = i
        
        for j in range(len(nums)):
            num = nums[j]
            if num in dic and dic[num] != j:
                other = nums[dic[num]]
                # result.append((value, num, other))
                # print(key, j, dic[num])
                if key != j and j != dic[num] and key != dic[num]:
                    result.append(tuple(sorted([nums[key], num, other])))
                    
                    
        # print('dictionary from Two sum:', value, dic)

        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        dic = {}
        for i in range(len(nums)):
            dic[0 - nums[i]] = i
        
        # def twoSum(key, target):
        #     dic = {}
        #     dic_res = {}

        #     result = []
        #     for i in nums:
        #         if i != key:
        #             if (target - i) not in dic:
        #                 dic[target - i] = [i]
        #             else:
        #                 dic[target - i].append(i)

        #     for i in nums:
        #         if i in dic:
        #             for j in range(len(dic[i])):
        #                 if key <= i and i <= dic[i][j]:
        #                     result.append((key, i, dic[i][j]))
        #     return result
            
        resulta = set()
        for key, val in dic.items():
            for i in self.twoSum(val, nums, key):
                resulta.add(i)
            # result.append([*twoSum(key, val)])
        # print('dictionary from three sum:', dic)

        return list(resulta)


