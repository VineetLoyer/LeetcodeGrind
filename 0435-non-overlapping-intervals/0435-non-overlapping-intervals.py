class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x[1])
        kept = 1
        end = intervals[0][1]

        for s,e in intervals[1:]:
            if s>=end:
                kept+=1
                end=e
        return len(intervals)-kept