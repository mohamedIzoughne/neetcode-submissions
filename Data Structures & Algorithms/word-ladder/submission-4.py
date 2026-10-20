from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
            
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, steps = queue.popleft()
            
            if word == endWord:
                return steps
            
            # Generate all possible neighbors
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char == word[i]: continue
                        
                    # Create the new word
                    new_word = word[:i] + char + word[i+1:]
                    
                    if new_word in word_set:
                        # Mark as visited by removing it from the set immediately
                        word_set.remove(new_word) 
                        queue.append((new_word, steps + 1))
                        
        return 0