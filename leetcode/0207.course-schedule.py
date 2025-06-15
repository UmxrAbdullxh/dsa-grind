class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for i in prerequisites:
            u,v = i
            graph[v].append(u)

        indegree = defaultdict(int)
        queue = []

        for node in graph:
            for nei in graph[node]:
                indegree[nei]= indegree[nei] + 1

        for node in graph:
            if indegree[node] == 0:
                queue.append(node)

        topological_order = []

        while queue:
            n = queue.pop(0)

            topological_order.append(n)

            for nei in graph[n]:
                indegree[nei] = indegree[nei] - 1
                
                # Add new 0 indegree nodes to queue
                if indegree[nei] == 0:
                    queue.append(nei)
        if len(topological_order) != len(graph):
            return False
        else:
            return True
       
