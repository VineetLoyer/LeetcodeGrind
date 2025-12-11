class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_bounds = {}
        col_bounds = {}

        # Pass 1: Determine the geometric bounds for every row and column
        for r, c in buildings:
            # Update Row Bounds
            if r not in row_bounds:
                row_bounds[r] = [c, c] # Initialize [min, max]
            else:
                if c < row_bounds[r][0]: row_bounds[r][0] = c # Update min
                if c > row_bounds[r][1]: row_bounds[r][1] = c # Update max

            # Update Column Bounds
            if c not in col_bounds:
                col_bounds[c] = [r, r] # Initialize [min, max]
            else:
                if r < col_bounds[c][0]: col_bounds[c][0] = r # Update min
                if r > col_bounds[c][1]: col_bounds[c][1] = r # Update max

        count = 0

        # Pass 2: Check coverage condition for each building
        for r, c in buildings:
            # A building is covered if it is strictly inside the min/max of its row AND column
            row_min, row_max = row_bounds[r]
            col_min, col_max = col_bounds[c]

            is_covered_horizontally = (c > row_min) and (c < row_max)
            is_covered_vertically   = (r > col_min) and (r < col_max)

            if is_covered_horizontally and is_covered_vertically:
                count += 1

        return count