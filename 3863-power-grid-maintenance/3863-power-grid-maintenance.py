from collections import defaultdict, deque
import heapq

class Solution:
    def processQueries(self, c, connections, queries):
        # 1. Build graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # 2. Component identification via BFS
        comp_id = [-1] * (c + 1)  # comp_id[i] == id of component containing i
        components = []
        curr_id = 0
        for i in range(1, c + 1):
            if comp_id[i] == -1:
                q = deque([i])
                comp = []
                comp_id[i] = curr_id
                while q:
                    node = q.popleft()
                    comp.append(node)
                    for nei in graph[node]:
                        if comp_id[nei] == -1:
                            comp_id[nei] = curr_id
                            q.append(nei)
                heapq.heapify(comp)  # min-heap per component
                components.append(comp)
                curr_id += 1
        
        # 3. Online/offline status array
        offline = [False] * (c + 1)

        # 4. Query processing
        ans = []
        for t, x in queries:
            cid = comp_id[x]
            comp_heap = components[cid]
            if t == 2:
                offline[x] = True
            else:
                if not offline[x]:
                    ans.append(x)
                else:
                    while comp_heap and offline[comp_heap[0]]:
                        heapq.heappop(comp_heap)
                    if comp_heap:
                        ans.append(comp_heap[0])
                    else:
                        ans.append(-1)
        return ans
