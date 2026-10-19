from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def check_similarity(word1, word2):
            word1_dic = {}
            word2_dic = {}

            for char in word1:
                if char in word1_dic:
                    word1_dic[char] += 1 
                else:
                    word1_dic[char] = 0
            
            for char in word2:
                if char in word2_dic:
                    word2_dic[char] += 1 
                else:
                    word2_dic[char] = 0


            counter = 0
            
            for char in word2:
                if char not in word1_dic or word1_dic[char] != word2_dic[char]:
                    counter += 1
            
            return False if counter > 1 else True
        
        wordList.append(beginWord)
        graph = {}

        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if i != j:
                    if check_similarity(wordList[i], wordList[j]):
                        if wordList[i] in graph:
                            graph[wordList[i]].append(wordList[j])
                        else:
                            graph[wordList[i]] = [wordList[j]]



        queue = deque([(beginWord, 1)])
        visited = set()


        while queue:
            word, traffic = queue.popleft()

            if word == endWord:
                return traffic
            visited.add(word)
            for neighbor in graph[word]:
                if neighbor not in visited:
                    queue.append((neighbor, traffic + 1))
        
        return 0






        
