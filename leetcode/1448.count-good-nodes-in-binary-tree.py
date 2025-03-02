# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root, maxV):
            if root.val >= maxV:
                self.count += 1
            root.left and dfs(root.left, max(root.val, maxV))
            root.right and dfs(root.right, max(root.val, maxV))
            return self.count
        res = dfs(root, float("-inf"))
        return res
        
