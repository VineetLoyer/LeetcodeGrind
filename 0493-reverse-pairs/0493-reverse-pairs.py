class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            if l >= r:
                return 0
            mid = (l + r) // 2
            count = merge_sort(l, mid) + merge_sort(mid + 1, r)

            # Count reverse pairs
            j = mid + 1
            for i in range(l, mid + 1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge step
            temp = []
            p1, p2 = l, mid + 1
            while p1 <= mid and p2 <= r:
                if nums[p1] <= nums[p2]:
                    temp.append(nums[p1])
                    p1 += 1
                else:
                    temp.append(nums[p2])
                    p2 += 1
            while p1 <= mid:
                temp.append(nums[p1])
                p1 += 1
            while p2 <= r:
                temp.append(nums[p2])
                p2 += 1
            nums[l:r + 1] = temp
            return count

        return merge_sort(0, len(nums) - 1)