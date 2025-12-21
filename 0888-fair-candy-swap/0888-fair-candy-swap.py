class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # Approach 1: At the end both should have same amount of candies. so. basically average. 
        # So, return [arr[i],arr[j]] when 

        s1 = sum(aliceSizes)
        s2 = sum(bobSizes)
        z = (s1-s2)//2
        aliceSet = set(aliceSizes)

        for y in bobSizes:
            target_x = y + z
            if target_x in aliceSet:
                return [target_x, y]
                
