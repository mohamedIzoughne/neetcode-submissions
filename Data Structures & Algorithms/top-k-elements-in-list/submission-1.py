class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## brute solution

        repeats = {}
        val_repeats = {}

        for i in nums:
            if i in repeats:
                repeats[i] += 1
            else:
                repeats[i] = 1
        
        for key, val in repeats.items():
            if val in val_repeats:
                val_repeats[val].append(key)
            else:
                val_repeats[val] = [key]
        
        # values = val_repeats.keys()
        maximums = []
        i = 0
        while i < k:

            maxi = float("-inf")
            for value in val_repeats.keys():
                maxi = max(maxi, value)
            # print(maximums,val_repeats.keys())
            
            for value in val_repeats[maxi]:
                maximums.append(value)
                if len(maximums) == k:
                    return maximums

            del val_repeats[maxi]
            i += 1
        
        return maximums
                    
