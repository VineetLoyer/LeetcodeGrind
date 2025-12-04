class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)

        # 1. count all moving cars
        moving = sum(1 for c in directions if c != 'S')

        # 2. count leading 'L's
        left_L = 0
        i = 0
        while i < n and directions[i] == 'L':
            left_L += 1
            i += 1

        # 3. count trailing 'R's
        right_R = 0
        j = n - 1
        while j >= 0 and directions[j] == 'R':
            right_R += 1
            j -= 1

        # 4. result
        return moving - left_L - right_R