class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        maximum = 0
        max_str = ""

        for i in range(len(s)):
            # Your smart pruning: stop when remaining length is less than or equal to `maximum`
            for j in range(len(s) - 1, i - 1 + maximum, -1):
                sub = s[i:j+1]
                
                # Python's built-in slice reverse is infinitely faster than a manual while loop
                if sub == sub[::-1]:
                    if len(sub) > maximum:
                        maximum = len(sub)
                        max_str = sub
                    # Break immediately because any further `j` will just be a shorter substring
                    break 

        return max_str