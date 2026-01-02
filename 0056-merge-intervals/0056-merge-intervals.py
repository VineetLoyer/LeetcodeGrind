class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        #1. Sort intervals by start.
        intervals.sort(key=lambda x:x[0])

        #2.Initialize a result list merged and push the first interval.
        merged = [intervals[0]]

        #3.For each next interval curr:
        for start,end in intervals[1:]:
            #4.Let last be the last interval in merged.
            last_start,last_end = merged[-1]
            #5.If curr[0] <= last[1], they overlap:
            if start<=last_end:
            #6.Update last[1] = max(last[1], curr[1]).
                merged[-1][1] = max(last_end,end)
            #7.Else (no overlap):
            else:
                #8.Append curr to merged.
                merged.append([start,end])
        return merged