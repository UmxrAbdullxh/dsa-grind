class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}

        def prim_weight_only(adj):
            nodes = list(adj.keys())
            n = len(nodes)
            if n <= 0:
                return 0
            start = nodes[0]  # pick any starting node
            
            visited = {node: False for node in nodes}
            min_heap = [(0, start)]
            mst_weight = 0

            while min_heap:
                w, u = heapq.heappop(min_heap)
                if visited[u]:
                    continue
                visited[u] = True
                mst_weight += w
                for v, weight in adj[u]:
                    if not visited[v]:
                        heapq.heappush(min_heap, (weight, v))

            return mst_weight

        for i in range(len(points)):
            for j in range(len(points)):
                if points[i] != points[j]:
                    x1, y1 = points[i][0], points[i][1]
                    x2, y2 = points[j][0], points[j][1]

                    weight = abs(x1-x2) + abs(y1-y2)

                    if (x1, y1) in adj:
                        adj[(x1,y1)].append(((x2, y2), weight))
                    else:
                        adj[(x1,y1)] = [((x2, y2), weight)]
        res = prim_weight_only(adj)
        return res
                
