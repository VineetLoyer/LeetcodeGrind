class Solution:
    def reverseWords(self, s: str) -> str:
        #intuition: 
        # 1. Trim leading and trailing spaces from the string.
        s=s.strip()
        # 2. Split the string into words (using whitespace as a separator).
        words=s.split()
        # 3. Reverse the list of words.
        words.reverse()
        # 4. Join the words using a single space.
        return " ".join(words)
        
        
        
        