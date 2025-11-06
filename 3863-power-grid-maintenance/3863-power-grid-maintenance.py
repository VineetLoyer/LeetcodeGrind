from collections import defaultdict
from bisect import bisect_left, insort
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y):
        self.parent[self.find(y)] = self.find(x)

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)
        for u, v in connections:
            uf.union(u, v)
        
        # Group all stations by their root (component id)
        comp_to_nodes = defaultdict(list)
        for i in range(1, c+1):
            root = uf.find(i)
            comp_to_nodes[root].append(i)
        
        # For each component, keep a sorted list of online stations
        from sortedcontainers import SortedList  # for very efficient removal and min finding
        comp_online = {}
        for comp, nodes in comp_to_nodes.items():
            comp_online[comp] = SortedList(nodes)
        
        offline = set()
        res = []
        for t, x in queries:
            root = uf.find(x)
            online = comp_online[root]
            if t == 2:
                if x not in offline:
                    idx = online.bisect_left(x)
                    if idx < len(online) and online[idx] == x:
                        online.pop(idx)
                    offline.add(x)
            else:
                if x not in offline:
                    res.append(x)
                elif online:
                    res.append(online[0])
                else:
                    res.append(-1)
        return res
