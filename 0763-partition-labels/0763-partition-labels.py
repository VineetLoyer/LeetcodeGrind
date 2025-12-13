class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #hashmap to store last index of characters
        last_index = {char: i for i,char in enumerate(s) }

        left = 0
        right = 0
        result = []
        for i, char in enumerate(s):
            right = max(right,last_index[char])
            if i==right:
                current_partition_size = right-left+1
                result.append(current_partition_size)
                left = i+1
        return result