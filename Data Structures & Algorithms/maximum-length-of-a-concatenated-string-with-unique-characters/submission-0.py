class Solution:
    def maxLength(self, arr: List[str]) -> int:
        

        def repeating(string):
            hash_set = set()

            for char in string:
                if char in hash_set:
                    return False
                hash_set.add(char)
            return True

        def backtrack(string, have):
            if not repeating(string):
                return 0
            
            maximum = len(string)
            
            for i in range(len(arr)):
                if i not in have:
                    have.add(i)

                    maximum = max(maximum, backtrack(string + arr[i], have))
                    have.remove(i)
            
            return maximum
        

        maximum = 0

        for stri in arr:
            maximum = max(maximum, backtrack(stri, set()))
        
        return maximum

            
