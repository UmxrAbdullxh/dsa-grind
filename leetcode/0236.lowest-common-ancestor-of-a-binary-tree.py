# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCS(root):
            if not root or root == p or root == q:
                return root
            left = LCS(root.left)
            right = LCS(root.right)

            if left and right:
                return root
            return left or right
        return LCS(root)
        