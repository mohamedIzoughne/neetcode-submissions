class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        table = [[False] * n for _ in range(n) ]

        count = 0

        for i in range(n-1, -1, -1):
            
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or s[i + 1][j - 1]):
                    table[i][j] = True
                    count += 1
        
        
         # for i in range(n):
        #     for j in range(n):
        #         if table[i][j] :
        #             count += 1
                    
        
        return count