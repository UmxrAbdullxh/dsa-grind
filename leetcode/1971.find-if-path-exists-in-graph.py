class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        def dfs(graph, source, destination, visited):
            if source == destination:
                return True

            if source in visited:
                return False

            visited.add(source)
            
            for nxt in graph[source]:
                if(dfs(graph, nxt, destination, visited) == True):
                    return True

            return False
            
        return dfs(graph, source, destination, set())


