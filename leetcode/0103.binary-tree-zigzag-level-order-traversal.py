# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        queue_counter = 0
        while queue:
            queue_size = len(queue)
            queue_level = []
            for i in range(queue_size):
                node = queue.popleft()
                queue_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue_counter % 2 == 0:
                result.append(queue_level)
            else:
                result.append(queue_level[::-1])
            queue_counter += 1
        return result
        