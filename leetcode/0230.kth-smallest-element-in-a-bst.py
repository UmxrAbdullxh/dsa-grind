# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        def dfs(root):
            root.left and dfs(root.left)
            values.append(root.val)
            root.right and dfs(root.right)
            return values
        res = dfs(root)
        return res[k-1]
        
