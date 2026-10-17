class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        dictt = {}

        for stri in strs:
            tup = [0] * 28
            # print(ord(j) - 65)
            for j in stri:
                tup[ord(j) - 95] = tup[ord(j) - 95] + 1
            
            tup = tuple(tup)
            if tup in dictt:
                dictt[tup].append(stri)
            else:
                dictt[tup] = [stri]
            
        return list(dictt.values())
        


