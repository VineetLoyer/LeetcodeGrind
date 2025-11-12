class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t) Brute force: O(nlogn + mlogm)
        # Use hashmap
        if len(s)!=len(t):
            return False
        countS,countT={},{} # make two hashmaps
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        return countS==countT # O(n+m)time and O(1) space as we are considering only 26 characters and lowercase