from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. Cleaned up similarity check (words are guaranteed to be same length)
        def check_similarity(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        # WordList as a set removes duplicates and gives O(1) lookups if needed later
        wordList.append(beginWord)
        graph = {}

        # 2. Build graph using your O(N^2) approach
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if i != j:
                    if check_similarity(wordList[i], wordList[j]):
                        if wordList[i] not in graph:
                            graph[wordList[i]] = []
                        graph[wordList[i]].append(wordList[j])

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])  # FIX: Add beginWord to visited initially

        while queue:
            word, traffic = queue.popleft()
            
            if word == endWord:
                return traffic
            
            if word in graph:            
                for neighbor in graph[word]:
                    if neighbor not in visited:
                        visited.add(neighbor)  # FIX: Mark visited BEFORE queueing
                        queue.append((neighbor, traffic + 1))
        
        return 0