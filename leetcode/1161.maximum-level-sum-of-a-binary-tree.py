# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        max_queue_level = 0
        max_level_value = float("-inf")
        queue_level = 1
        queue = deque([root])
        while queue:
            queue_sum = 0
            queue_size = len(queue)
            for _ in range(queue_size):
                node = queue.popleft()
                queue_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue_sum > max_level_value:
                max_level_value = queue_sum
                max_queue_level = queue_level
            queue_level += 1
        return max_queue_level
    