class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []

        for src, dest, time in times:
            if src in adj:
                adj[src].append((dest, time))    
            else:
                adj[src] = [(dest, time)]

        def dijkstra(graph, start):
            # priority queue
            pq = [(0, start)]

            # dictioniary to store distances
            distances = {node: float("inf") for node in graph}
            distances[start] = 0

            while pq:
                current_distance, current_node = heapq.heappop(pq)

                if current_distance > distances[current_node]:
                    continue

                for neighbour, weight in graph[current_node]:
                    distance = weight + current_distance

                    if distances[neighbour] > distance:
                        distances[neighbour] = distance
                        heapq.heappush(pq, (distance, neighbour))

            return distances

        shortest = -1
        res = dijkstra(adj, k)
        for i in res:
            if res[i] == float("inf"):
                return -1
            shortest = max(res[i], shortest)
        return shortest
        
