class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += str(len(s))+ '#'+s
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return ""
        res = []
        i = 0
        while i<len(s): #traverse the concatenated string
            j = i # j traverses the individual strings
            while s[j]!='#':
                j+=1
            length = int(s[i:j]) # we extrace the length of the string convert it to int
            res.append(s[j+1:j+1+length]) #traverse after # till the length of string we extracted
            i = j+1+length 
        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))