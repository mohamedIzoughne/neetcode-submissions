class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 1:
            return s


        dic = {}
        maximum = 0

        for i in range(len(s)):
            for j in range(len(s) - 1, i -1  + maximum, -1):
                # word = s[i:j+1]
                sub = s[i:j+1]
                # print(maximum)
                if sub == sub[::-1]:

                    if j + 1 - i > maximum:
                        # print(maximum)
                        maximum = j + 1 - i
                        dic[j + 1 - i] = s[i:j+1]
                    break
                    
                
        maximum = 0
        for key in dic.keys():
            maximum = max(maximum, key)
        

        return dic[maximum] if maximum in dic else ""
