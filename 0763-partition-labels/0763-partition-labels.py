class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #hashmap to store last index of characters
        last_index = {char: i for i,char in enumerate(s) }

        left=  0
        right= 0
        res = []
        for i,char in enumerate(s):
            right=max(right,last_index[char])
            if i==right:
                res.append(right-left+1)
                left=i+1
        return res
