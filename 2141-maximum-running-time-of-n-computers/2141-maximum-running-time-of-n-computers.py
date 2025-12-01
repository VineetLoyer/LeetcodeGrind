class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total_power = sum(batteries)
        left, right = 0, total_power // n  # max possible minutes

        def can_run(T: int) -> bool:
            # total usable time if we try to run for T minutes
            usable = 0
            for b in batteries:
                usable += min(b, T)
                if usable >= n * T:  # early exit
                    return True
            return usable >= n * T

        while left < right:
            mid = (left + right + 1) // 2  # bias upward
            if can_run(mid):
                left = mid
            else:
                right = mid - 1

        return left