class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = version1.split('.')
        lst2 = version2.split('.')

        n = len(lst1)
        m = len(lst2)

        for i in range(max(n,m)):
            v1 = int(lst1[i]) if i<n else 0
            v2 = int(lst2[i]) if i<m else 0
            if v1<v2:
                return -1
            elif v1>v2:
                return 1
        return 0
            
