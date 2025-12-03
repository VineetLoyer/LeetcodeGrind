class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0

        # Normalize direction (slope) as a reduced integer pair
        def norm_dir(dx: int, dy: int) -> tuple[int, int]:
            g = gcd(dx, dy)
            dx //= g
            dy //= g
            # Fix sign so each slope has a unique representation
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy
            return dx, dy

        # edges[slope][line_id] = number of segments lying on that geometric line
        edges: dict[tuple[int, int], dict[int, int]] = defaultdict(lambda: defaultdict(int))
        # lines[(slope, line_id)] = set of point indices on that line
        lines: dict[tuple[tuple[int, int], int], set[int]] = defaultdict(set)

        # Enumerate all point pairs as segments, group by (slope, line)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                sx, sy = norm_dir(dx, dy)          # slope
                # Line invariant: (-sy) * x + sx * y is constant for a fixed line
                line_id = -sy * x1 + sx * y1
                edges[(sx, sy)][line_id] += 1
                lines[((sx, sy), line_id)].add(i)
                lines[((sx, sy), line_id)].add(j)

        # Count all quadrilaterals with at least one pair of parallel sides
        # For each slope s, we have several parallel lines; each line has e_i segments.
        # Number of ways to pick two segments on two different lines:
        # sum_{i<j} e_i * e_j = ((sum e_i)^2 - sum e_i^2) / 2
        total_traps = 0
        for mp in edges.values():
            if len(mp) < 2:
                continue
            s = 0
            s2 = 0
            for cnt in mp.values():
                s += cnt
                s2 += cnt * cnt
            total_traps += (s * s - s2) // 2

        # Now correct for parallelograms: each true parallelogram was counted twice
        # (once per each pair of parallel sides). We subtract the number of
        # non-degenerate parallelograms.

        def count_parallelograms(pts: List[List[int]]) -> int:
            m = len(pts)
            if m < 4:
                return 0
            mid_cnt = defaultdict(int)
            # Group all point pairs by (2 * midpoint)
            for i in range(m):
                x1, y1 = pts[i]
                for j in range(i + 1, m):
                    x2, y2 = pts[j]
                    mid_cnt[(x1 + x2, y1 + y2)] += 1
            res = 0
            for c in mid_cnt.values():
                if c > 1:
                    # choose 2 diagonals sharing the same midpoint
                    res += c * (c - 1) // 2
            return res

        # All parallelograms (including degenerate ones where 4 points are collinear)
        dup = count_parallelograms(points)

        # Remove degenerate "parallelograms" that lie on a single line:
        # those were not counted in total_traps in the first place.
        for idxs in lines.values():
            if len(idxs) >= 4:
                col_pts = [points[i] for i in idxs]
                dup -= count_parallelograms(col_pts)

        # Each genuine parallelogram was counted twice, so subtract their count once.
        return total_traps - dup