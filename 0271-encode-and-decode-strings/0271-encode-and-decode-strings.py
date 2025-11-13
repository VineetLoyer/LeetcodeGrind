class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""
        result = []
        for s in strs:
            result.append(str(len(s)) + '#' + s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return [""]
        i = 0
        result = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            result.append(s[j:j + length])
            i = j + length
        return result

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))