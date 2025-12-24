class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        need = sum(apple)
        capacity.sort(reverse=True)

        total = 0
        for i, c in enumerate(capacity, 1):
            total += c
            if total >= need:
                return i

        # If inputs could be infeasible, you could return -1 here.
        return len(capacity)