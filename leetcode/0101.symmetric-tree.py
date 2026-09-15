# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if p and not q:
                return False
            if p and q and p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        def invertTree(root):
            if not root:
                return None

            root.left, root.right = root.right, root.left

            invertTree(root.left)
            invertTree(root.right)

            return root

        return isSameTree(root.left, invertTree(root.right))
        