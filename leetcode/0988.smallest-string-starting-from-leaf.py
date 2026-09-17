# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode | None) -> str:
        result = "z"*26
        char_map = {i - ord('a'):chr(i) for i in range(ord('a'), ord('z') + 1)}
        def dfs(root, path):
            nonlocal result
            if not root:
                return None
            char = char_map[root.val]
            path = char + path
            if not root.left and not root.right:
                if path < result:
                    result = path
            dfs(root.left, path)
            dfs(root.right, path)
            return
        
        dfs(root, "")
        return result
        