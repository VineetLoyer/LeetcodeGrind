class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            countstring = [0]*26 
            for char in word:
                countstring[ord(char)-ord('a')]+=1
            key = tuple(countstring) #convert to tuple
            res[key].append(word) #then i append word to this new key
        return list(res.values())