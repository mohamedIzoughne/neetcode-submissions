from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        
        # Map intermediate states to words (e.g., "*at" -> ["cat", "bat", "sat"])
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
                
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            current_word, steps = queue.popleft()
            
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                
                for neighbor in all_combo_dict[intermediate_word]:
                    if neighbor == endWord:
                        return steps + 1
                        
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
                
                # Clear the list to save time on future lookups (pruning)
                all_combo_dict[intermediate_word] = []
                
        return 0