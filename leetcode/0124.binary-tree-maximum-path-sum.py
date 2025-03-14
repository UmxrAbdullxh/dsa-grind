# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            # compute max with split
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            #compare with -ve values
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute res
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # compute return without split

            return root.val + max(leftMax, rightMax)
    
        dfs(root)
        return res[0]
