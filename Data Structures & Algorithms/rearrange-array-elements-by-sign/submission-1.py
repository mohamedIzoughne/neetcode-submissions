class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        i = 0
        j = 1
        LENGTH = len(nums)
        while i < LENGTH - 1:
            j = i + 1

            if i % 2 == 0 and nums[i] < 0:
                while j < LENGTH -1 and nums[j] > 0:
                    j+= 1

                while j > i:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    j -= 1
                j = i + 1

            if nums[i] > 0 and nums[j] > 0:

                while nums[j] > 0:
                    j+= 1

                while j > i + 1:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    j -= 1
            i += 1
        
        return nums
                

            

