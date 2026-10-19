from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def check_similarity(word1, word2):
            mini = min(len(word1), len(word2))
            maxi = len(word1) + len(word2) - mini
            difference = maxi - mini
            counter = difference


            for i in range(mini):
                if word1[i] != word2[i]:
                    counter += 1
            
            return False if counter > 1 else True
        
        wordList.append(beginWord)

        # print(check_similarity("laaaa", "aaaaa"))

        # return 0
        graph = {}
        # print(wordList)

        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if i != j:
                    if check_similarity(wordList[i], wordList[j]):
                        if wordList[i] in graph:
                            graph[wordList[i]].append(wordList[j])
                        else:
                            graph[wordList[i]] = [wordList[j]]
            # if wordList[i] not in graph:
            #     graph[wordList[i]] = []


        # print(graph, beginWord in graph)
        queue = deque([(beginWord, 1)])
        visited = set()


        while queue:
            word, traffic = queue.popleft()
            # print(word, traffic)
            if word == endWord:
                return traffic
            
            visited.add(word)
            if word in graph:            
                for neighbor in graph[word]:
                    if neighbor not in visited:
                        queue.append((neighbor, traffic + 1))
        
        return 0






        
