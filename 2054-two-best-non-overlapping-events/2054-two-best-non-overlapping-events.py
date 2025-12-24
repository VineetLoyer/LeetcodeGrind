class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        by_start = sorted(events, key=lambda x: x[0])
        by_end   = sorted(events, key=lambda x: x[1])

        best_single = 0     # best value of a single event that ended before current start
        ans = 0
        j = 0               # pointer in by_end

        for s, e, v in by_start:
            # advance j to include all events that end < s (strictly less: non-overlap with inclusive end)
            while j < len(by_end) and by_end[j][1] < s:
                best_single = max(best_single, by_end[j][2])
                j += 1
            # either take this event alone or pair with the best compatible earlier one
            ans = max(ans, v, best_single + v)

        return ans