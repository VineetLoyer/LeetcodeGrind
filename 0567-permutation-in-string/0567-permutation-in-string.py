class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        counter2 = Counter(s2[:len(s1)])
        for i in range(len(s2)-len(s1)+1):
            if counter1==counter2:
                return True
            if i+len(s1)<len(s2):
                left_char = s2[i]
                right_char = s2[i+len(s1)]
                counter2[right_char]+=1
                counter2[left_char]-=1
                if counter2[left_char]==0:
                    del counter2[left_char]
        return False