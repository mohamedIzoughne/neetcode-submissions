class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""

        start, max_len = 0, 0

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the found palindrome
            return right - left - 1

        for i in range(len(s)):
            # Odd length palindromes (center is a single char)
            len1 = expand_around_center(i, i)
            # Even length palindromes (center is between chars)
            len2 = expand_around_center(i, i + 1)
            
            curr_max = max(len1, len2)
            if curr_max > max_len:
                max_len = curr_max
                # Calculate the starting index of the palindrome
                start = i - (curr_max - 1) // 2
                
        return s[start:start + max_len]