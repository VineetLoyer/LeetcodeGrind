class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        s0, e0 = intervals[0]
        p1 = e0 - 1   # second largest chosen point
        p2 = e0       # largest chosen point
        ans = 2
        for s, e in intervals[1:]:
            if s <= p1:
                # Case A: already has p1 and p2
                continue
            elif s <= p2:
                # Case B: only p2 inside -> add one more point
                ans += 1
                p1, p2 = p2, e
            else:
                # Case C: no point inside -> add two points
                ans += 2
                p1, p2 = e - 1, e

        return ans