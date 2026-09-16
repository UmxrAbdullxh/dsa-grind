# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        result = []
        def dfs(root, path):            
            path += str(root.val)
            if root and (root.left or root.right):
                path += "->"
            if root and not root.left and not root.right:
                result.append(path)
                return
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)

            return

        dfs(root, "")
        return result
        