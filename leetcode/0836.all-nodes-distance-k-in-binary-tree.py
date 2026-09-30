# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {root: None}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in (node.left, node.right):
                if child:
                    parent[child] = node
                    stack.append(child)

        visited = {target}
        queue = deque([(target, 0)])
        while queue:
            if queue[0][1] == k:
                return [node.val for node, _ in queue]
            node, dist = queue.popleft()
            for nxt in (node.left, node.right, parent[node]):
                if nxt and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, dist+1))
        
        return []
        