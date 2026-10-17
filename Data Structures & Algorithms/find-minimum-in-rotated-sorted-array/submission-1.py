class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        med = len(nums) // 2
        first = 0
        last = len(nums) - 1
        while first + 1 < last:
            if nums[first] < nums[med] and nums[med] < nums[last]:
                last = med
                med = (med + first) // 2
                # return nums[first]
            elif nums[med] > nums[last]:
                # go right
                first = med
                med = (last + med + 1) // 2

            elif nums[med] < nums[first]:
                # go left
                last = med
                med = (med + first) // 2
        
        if nums[first] > nums[last]:
            return nums[last]
        else:
            return nums[first]
        # return nums[med]
            















