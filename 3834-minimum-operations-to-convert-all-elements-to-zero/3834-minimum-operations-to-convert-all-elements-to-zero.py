class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # Nearest strictly smaller to the left
        left_less = [-1] * n
        st = []
        for i, x in enumerate(nums):
            while st and nums[st[-1]] >= x:  # pop >= to ensure "strictly smaller"
                st.pop()
            left_less[i] = st[-1] if st else -1
            st.append(i)

        # Nearest strictly smaller to the right
        right_less = [n] * n
        st = []
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while st and nums[st[-1]] >= x:  # pop >= for "strictly smaller"
                st.pop()
            right_less[i] = st[-1] if st else n
            st.append(i)

        # For each value a>0, count distinct (L,R) among indices with value a
        buckets = defaultdict(set)  # value -> set of (L,R)
        for i, x in enumerate(nums):
            if x > 0:
                buckets[x].add((left_less[i], right_less[i]))

        return sum(len(s) for s in buckets.values())