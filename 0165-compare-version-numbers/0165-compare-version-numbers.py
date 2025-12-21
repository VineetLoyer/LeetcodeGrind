class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")

        n1,n2 = len(nums1),len(nums2)
        for i in range(max(n1,n2)):
            v1=int(nums1[i]) if i<n1 else 0
            v2=int(nums2[i]) if i<n2 else 0

            if v1<v2:
                return -1
            elif v1>v2:
                return 1
        return 0