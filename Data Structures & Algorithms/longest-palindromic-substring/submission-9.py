class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        table = [[False] * n for _ in range(n)]
        resInd = 0
        resLen = 0
        for i in range(n - 1, -1, -1):

            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or table[i+1][j-1]):
                    table[i][j] = True
                    if j - i > resLen:
                        resLen = j - i
                        resInd = i
            
        return s[resInd:resInd + resLen + 1]

