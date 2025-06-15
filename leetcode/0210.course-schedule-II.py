class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegree = defaultdict(int)
        queue = []
        topological_order = []
        
        for course in range(numCourses):
            graph[course] = []

        for p in prerequisites:
            u,v = p
            graph[v].append(u)

        for node in graph:
            for nei in graph[node]:
                indegree[nei] += 1

        for node in graph:
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            n = queue.pop(0)
            topological_order.append(n)

            for nei in graph[n]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        if len(topological_order) != len(graph):
            return []
        else:
            return topological_order



