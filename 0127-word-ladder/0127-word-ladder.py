class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # use BFS - why? it explores all possible "steps" from starting point, one layer at a time (precisely what we need)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0 #early exit if the endWord is not in wordList at all
        
        #BFS Implementation
        queue = deque()
        queue.append((beginWord,1))
        visited=set([beginWord])

        while queue:
            current_word, current_length = queue.popleft()
            # For each position, try changing to every possible letter
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word == endWord:
                        return current_length + 1  # Found endWord!
                    if next_word in wordSet and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, current_length + 1))
        # Step 4: If queue empties and there's no path, return 0
        return 0
