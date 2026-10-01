# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDeleteMap = {}
        result = []
        for i in to_delete:
            toDeleteMap[i] = True
        def dfs(root):
            if not root:
                return None
            left = dfs(root.left)
            right = dfs(root.right)

            if root.val in toDeleteMap:
                if root.left and left:
                    result.append(root.left)
                if root.right and right:
                    result.append(root.right)
                return None
            if not left:
                root.left = None
            if not right:
                root.right = None
            return root
        parent = dfs(root)
        if parent:
            result.append(parent)
        return result
        