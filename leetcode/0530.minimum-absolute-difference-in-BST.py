# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = 0
        result = float("inf")
        isFirstNode = True
        def dfs(root):
            nonlocal result, prev, isFirstNode
            if not root:
                return None
            dfs(root.left)
            if isFirstNode == False:
                diff = root.val - prev
                result = min(result, diff)
            prev = root.val
            if isFirstNode:
                isFirstNode = False
            dfs(root.right)
            return None
        dfs(root)
        return result
        