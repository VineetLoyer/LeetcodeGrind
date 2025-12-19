class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])

        know = set([0, firstPerson])

        i = 0
        while i < len(meetings):
            t = meetings[i][2]

            # Collect all meetings at time t
            people = set()
            j = i
            while j < len(meetings) and meetings[j][2] == t:
                x, y, _ = meetings[j]
                people.add(x)
                people.add(y)
                j += 1

            # DSU for this time block only
            parent = {p: p for p in people}
            rank = {p: 0 for p in people}

            def find(a):
                while parent[a] != a:
                    parent[a] = parent[parent[a]]
                    a = parent[a]
                return a

            def union(a, b):
                ra, rb = find(a), find(b)
                if ra == rb:
                    return
                if rank[ra] < rank[rb]:
                    parent[ra] = rb
                elif rank[ra] > rank[rb]:
                    parent[rb] = ra
                else:
                    parent[rb] = ra
                    rank[ra] += 1

            # Union all meetings at time t
            for k in range(i, j):
                x, y, _ = meetings[k]
                union(x, y)

            # Group members by component root
            comps = {}
            for p in people:
                r = find(p)
                comps.setdefault(r, []).append(p)

            # If a component has anyone who knows, everyone in it learns
            for members in comps.values():
                if any(m in know for m in members):
                    know.update(members)

            i = j

        return list(know)