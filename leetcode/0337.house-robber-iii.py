# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(root):
            if not root:
                return (0, 0)
            l_rob, l_skip = dfs(root.left)
            r_rob, r_skip = dfs(root.right)
            # rob current node, so we are not picking the value of robbed from children
            this_rob = root.val + l_skip + r_skip
            this_skip = max(l_rob, l_skip) + max(r_rob, r_skip)
            return (this_rob, this_skip)
        return max(dfs(root))
        